import scrapy
from bs4 import BeautifulSoup
from movie_test.items import MovieItem
import re
class GetMovieSpider(scrapy.Spider):
    name = "get_movie"  # 爬虫名称
    allowed_domains = ["movie.douban.com"]  # 允许的域名
    start_urls = ["https://movie.douban.com/top250"]  # 起始 URL
    redis_key = "get_movie:start_urls"  # Redis 中的起始 URL 键
    # 正则表达式
    findLink = re.compile(r'<a href="(.*?)">')
    findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
    findTitle = re.compile(r'<span class="title">(.*)</span>')
    findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
    findJudge = re.compile(r'<span>(\d*)人评价</span>')
    findInq = re.compile(r'<span class="inq">(.*)</span>')
    findBd = re.compile(r'<p class="">(.*?)</p>', re.S)
    def parse(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
        for item in soup.find_all('div', class_="item"):
            movie = MovieItem()
            item = str(item)
            movie['info_link'] = re.findall(self.findLink, item)[0]
            movie['pic_link'] = re.findall(self.findImgSrc, item)[0]
            titles = re.findall(self.findTitle, item)
            if len(titles) == 2:
                movie['cname'] = titles[0]
                movie['ename'] = titles[1].replace("/", "")
            else:
                movie['cname'] = titles[0]
                movie['ename'] = ' '
            movie['score'] = re.findall(self.findRating, item)[0]
            movie['rated'] = re.findall(self.findJudge, item)[0]
            inq = re.findall(self.findInq, item)
            movie['instroduction'] = inq[0].replace("。", "") if inq else " "
            bd = re.findall(self.findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', "", bd)
            bd = re.sub('/', "", bd)
            movie['info'] = bd.strip()
            yield movie
        # 处理分页
        next_page = response.css('span.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
