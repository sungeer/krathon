import time

from krathon.utils.log_util import logger
from krathon.tasks.huey_instance import huey


@huey.task()
def long_running_task():
    logger.info('Starting long-running task...')
    time.sleep(20)
    logger.info('Long-running task completed!')
