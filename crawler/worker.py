# 启动 Celery Worker

import os

print("🚀 启动 Celery Worker...")
os.system("celery -A crawler.tasks worker --loglevel=info")