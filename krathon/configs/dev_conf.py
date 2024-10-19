from krathon.configs.base_conf import BaseSettings


class DevSettings(BaseSettings):
    env = 'dev'

    # mysql
    db_name = 'viper'
    db_port = 3306
    db_host = '127.0.0.1'

    redis_host = '127.0.0.1'
