import multiprocessing
import subprocess
def run_spider(spider_name):
    subprocess.run(['scrapy', 'crawl', spider_name])
if __name__ == '__main__':
    spiders = ['get_movie']  # 如果有多个爬虫，可以添加到列表中
    processes = []
    for spider in spiders:
        p = multiprocessing.Process(target=run_spider, args=(spider,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
