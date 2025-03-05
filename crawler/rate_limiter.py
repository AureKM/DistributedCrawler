# 请求频率控制

import time

class RateLimiter:
    def __init__(self, interval):
        self.interval = interval
        self.last_time = 0

    def wait(self):
        now = time.time()
        wait_time = self.interval - (now - self.last_time)
        if wait_time > 0:
            time.sleep(wait_time)
        self.last_time = time.time()