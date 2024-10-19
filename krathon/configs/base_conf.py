from pathlib import Path


class BaseSettings:
    app_name = 'krathon'

    # Path(__file__).resolve() 获取当前文件的绝对路径
    # parents 属性获取上级目录
    # [2] 获取 上上上级目录
    basedir = Path(__file__).resolve().parents[2]

    jwt_algorithm = 'HS256'  # 加密算法
    access_token_expire_minutes = 1440  # token 有效期 1440 即 24h

    ai_url = 'https://ai-api.betteryeah.com'
