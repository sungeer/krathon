from huey import RedisHuey
from redis import ConnectionPool

from krathon.configs import settings
from krathon.tasks.log_config import logger

connection_pool = ConnectionPool(
    host=settings.redis_host,
    port=6379,
    password=settings.redis_passwd,
    db=0
)

huey = RedisHuey(settings.app_name, connection_pool=connection_pool, blocking=True)

# 在消费者 启动时 加载 定时任务
from krathon.tasks import scheduled_tasks
