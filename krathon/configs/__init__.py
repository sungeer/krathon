import os

from dotenv import load_dotenv

from krathon.configs.dev_conf import DevSettings
from krathon.configs.prod_conf import ProdSettings

config = {
    'dev': DevSettings,
    'prod': ProdSettings,
}


def get_settings():
    load_dotenv()  # 项目运行的目录
    config_name = os.getenv('FLASK_ENV', 'prod')
    configs = config[config_name]()  # oop
    envs = ['SEC_KEY', 'JWT_SECRET_KEY', 'DB_USER', 'DB_PASS', 'AI_API_KEY', 'REDIS_PASSWD', 'AI_WORKSPACE_ID', 'AI_ROBOT_ID']
    envs_dict = {}
    for env in envs:
        key = env.lower()
        value = os.getenv(env)  # sec_key = os.environ['SEC_KEY']
        envs_dict.update({key: value})
    for key, value in envs_dict.items():
        setattr(configs, key, value)  # setattr(configs, 'sec_key', sec_key)
    return configs


settings = get_settings()
