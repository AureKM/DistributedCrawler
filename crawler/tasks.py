# Celery 任务定义

from celery import Celery
import requests
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser
from crawler.rate_limiter import RateLimiter
import time

# 初始化 Celery（使用 Redis 作为消息队列）
app = Celery('crawler', broker='redis://localhost:6379/0')

# 频率限制器（防止爬虫爬太快被封）
rate_limiter = RateLimiter(1)  # 每个请求至少间隔 1 秒

def check_robots(url):
    """检查 robots.txt 规则，判断是否允许爬取"""
    domain = url.split('/')[2]
    rp = RobotFileParser()
    rp.set_url(f"https://{domain}/robots.txt")
    try:
        rp.read()
        return rp.can_fetch("*", url)
    except:
        return True  # 默认允许爬取

@app.task
def fetch_url(url):
    """爬取网页，提取标题，并发送给解析模块"""
    if not check_robots(url):
        print(f"❌ 不能爬取: {url}")
        return None

    rate_limiter.wait()  # 控制爬取速率

    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.find("title").text if soup.find("title") else "No Title"
            print(f"✅ 爬取成功: {url} -> {title}")

            # 发送数据给解析模块（模拟）
            requests.post("http://localhost:5001/parse_data", json={"url": url, "title": title})
            return title
        else:
            print(f"❌ 请求失败: {url} (状态码: {response.status_code})")
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ 爬取失败: {url}, 错误: {e}")
        return None