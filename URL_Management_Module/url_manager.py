import redis
from flink_url_processor import FlinkURLProcessor
from redis_url_queue import RedisURLQueue

class URLManager:
    def __init__(self, seed_file, redis_host='localhost', redis_port=6379):
        self.seed_file = seed_file
        self.redis_queue = RedisURLQueue(redis_host, redis_port)
        self.flink_processor = FlinkURLProcessor()

    def load_seed_urls(self):
        """从种子文件中加载 URL"""
        with open(self.seed_file, 'r') as file:
            urls = [line.strip() for line in file if line.strip()]
        return urls

    def process_urls(self):
        """处理 URL：去重并存储到 Redis"""
        seed_urls = self.load_seed_urls()
        unique_urls = self.flink_processor.deduplicate_urls(seed_urls)
        for url in unique_urls:
            self.redis_queue.push(url)
        print(f"Processed {len(unique_urls)} unique URLs.")

if __name__ == "__main__":
    manager = URLManager(seed_file='seed_urls.txt')
    manager.process_urls()