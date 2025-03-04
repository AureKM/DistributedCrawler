import redis

class RedisURLQueue:
    def __init__(self, host='localhost', port=6379, db=0):
        self.client = redis.Redis(host=host, port=port, db=db)

    def push(self, url):
        """将 URL 添加到 Redis 队列"""
        self.client.lpush('url_queue', url)

    def pop(self):
        """从 Redis 队列中获取 URL"""
        return self.client.rpop('url_queue')

    def size(self):
        """获取队列大小"""
        return self.client.llen('url_queue')