# DistributedCrawler
分布式爬虫系统

## 项目介绍
基于Flink+kafka/redis+爬虫框架+存储实现一个简易分布式爬虫系统，通过Flink流式计算实现待爬取url的去重，接着将去重后的url发送到kafka或者redis消息队列里，然后再把url分发给各个爬虫节点，经过解析处理后将数据存到数据库。

