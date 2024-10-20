import time

from krathon.tasks.log_config import logger
from krathon.tasks.huey_instance import huey


@huey.task()
def long_running_task():
    logger.info('Starting long-running task...')
    time.sleep(20)
    logger.info('Long-running task completed!')
