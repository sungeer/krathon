from huey import RedisHuey
from redis import ConnectionPool

from krathon.configs import settings

connection_pool = ConnectionPool(
    host=settings.redis_host,
    port=6379,
    password=settings.redis_passwd,
    db=0
)

huey = RedisHuey(settings.app_name, connection_pool=connection_pool)
