import os
from pathlib import Path

from dotenv import load_dotenv

from kimi.utils.conf_util import ConfigDetector

CURRENT_DIR = Path(__file__).resolve()  # 当前文件 的 绝对路径
BASE_DIR = CURRENT_DIR.parent.parent.parent

load_dotenv()

DEBUG = os.getenv('DEBUG')

if DEBUG:
    conf_dir = BASE_DIR / 'nacos-data'
    CONF = ConfigDetector(conf_dir)
else:
    CONF = ConfigDetector(
        nacos_addr=os.getenv('NACOS_ADDR'),
        namespace=os.getenv('NACOS_NAMESPACE')
    )
