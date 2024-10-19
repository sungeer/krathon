from huey import crontab

from krathon.utils.log_util import logger
from krathon.tasks.huey_instance import huey


@huey.periodic_task(crontab(minute='0', hour='3'))  # 每天凌晨3点执行一次
def scheduled_task():
    logger.info('Scheduled task running...')


@huey.periodic_task(crontab())  # 每分钟执行一次
def every_minute_task():
    logger.info('Task running every minute...')
