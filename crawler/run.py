# 触发爬取任务

from crawler.tasks import fetch_url

# 待爬取的 URL 列表（后续可从 A 组 API 获取）
urls = [
    "https://baidu.com",
    "https://juejin.cn",
    "https://github.com"
]

# 发送爬取任务到 Celery
for url in urls:
    fetch_url.delay(url)  # 异步执行
    print(f"📡 任务已发送: {url}")