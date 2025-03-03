# Scrapy settings for movie_test project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "movie_test"

SPIDER_MODULES = ["movie_test.spiders"]
NEWSPIDER_MODULE = "movie_test.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "movie_test.middlewares.MovieTestSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "movie_test.middlewares.MovieTestDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "movie_test.pipelines.MovieTestPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# 设置去重组件
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 调度组件
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
REDIS_URL = 'redis://localhost:6379'

#redis 连接信息
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
REDIS_ENCODING = 'utf-8'
#REDIS_PARAMS = {"password":"123456"}
#断点续爬
SCHEDULER_PERSIST = True

BOT_NAME = "movie_test"
SPIDER_MODULES = ["movie_test.spiders"]
NEWSPIDER_MODULE = "movie_test.spiders"
# 启用 Pipeline
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 400,
    'movie_test.pipelines.MoviePipeline': 300,
}

# 启用 Cookies
COOKIES_ENABLED = True
# 设置默认的 Cookie
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': "",
    'Referer': 'https://movie.douban.com/',
     'Cookie': "",
}
DOWNLOAD_DELAY = 2  # 每 2 秒发送一个请求
RANDOMIZE_DOWNLOAD_DELAY = True
PROXY_POOL_ENABLED = True #使用代理
# 遵守爬虫协议
ROBOTSTXT_OBEY = False
#启动中间件
DOWNLOADER_MIDDLEWARES = {
    'movie_test.middlewares.CustomRedirectMiddleware': 600,
    'movie_test.middlewares.DebugMiddleware': 800,
}
#禁用 robots.txt
ROBOTSTXT_OBEY = False
#轮询策略
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.RoundRobinQueue'
#使用哈希策略
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
