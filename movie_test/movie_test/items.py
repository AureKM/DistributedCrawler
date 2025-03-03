import scrapy
class MovieItem(scrapy.Item):
    info_link = scrapy.Field()      # 电影详情链接
    pic_link = scrapy.Field()       # 图片链接
    cname = scrapy.Field()          # 中文名
    ename = scrapy.Field()          # 外文名
    score = scrapy.Field()          # 评分
    rated = scrapy.Field()          # 评价数
    instroduction = scrapy.Field()  # 简介
    info = scrapy.Field()           # 相关信息
