import sys
import logging
from pathlib import Path

from loguru import logger

from krathon.configs import settings

log_dir = Path(settings.basedir).joinpath('logs')
log_dir.mkdir(parents=True, exist_ok=True)

huey_path = log_dir.joinpath('huey.log')  # 'logs/huey.log'

logger.remove()

logger.add(
    huey_path,
    rotation='50MB',
    format='{time:YYYY-MM-DD HH:mm:ss} - {level} - {message}',
    encoding='utf-8',
    enqueue=True,  # 启用异步日志处理
    diagnose=False,  # 关闭变量值
    backtrace=False,  # 关闭完整堆栈跟踪
    colorize=False,
    level='INFO'
)

logger.add(
    sink=sys.stdout,
    format='{time:YYYY-MM-DD HH:mm:ss} - {level} - {message}',
    diagnose=False,
    backtrace=False,
    colorize=False,
    enqueue=True,
    level='INFO'
)


# 将 Huey 的日志记录器与 loguru 连接
class InterceptHandler(logging.Handler):

    def emit(self, record):
        loguru_logger = logger.bind()  # 获取 loguru 的日志记录器

        # 将标准的 logging 日志记录转换为 loguru 格式
        loguru_logger_opt = loguru_logger.opt(depth=6, exception=record.exc_info)
        loguru_logger_opt.log(record.levelname, record.getMessage())


huey_logger = logging.getLogger('huey')
huey_logger.setLevel(logging.INFO)
huey_logger.addHandler(InterceptHandler())
