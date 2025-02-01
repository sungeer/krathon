from datetime import datetime, timedelta

import bcrypt  # python -m pip install bcrypt
import jwt  # python -m pip install pyjwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from quart import current_app

from kimi.utils.errors import TokenExpiredError, AuthenticationError

config = current_app.config


def set_password(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')


def validate_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


def generate_token(data: dict):
    token_data = data.copy()  # data = {'id': 3}
    expiration_delta = timedelta(minutes=config.get_int_conf('JWT', 'EXPIRE_MINUTES'))
    expiration_time = datetime.now() + expiration_delta
    token_data.update({'exp': expiration_time.timestamp()})
    encoded_token = jwt.encode(
        token_data, config.get_conf('JWT', 'SEC_KEY'),
        algorithm=config.get_conf('JWT', 'ALGORITHM')
    )
    return encoded_token


def verify_token(token: str):
    secret_key = config.get_conf('JWT', 'SEC_KEY')
    jwt_algorithm = config.get_conf('JWT', 'ALGORITHM')
    try:
        payload = jwt.decode(token, secret_key, algorithms=[jwt_algorithm])
        user_id = payload.get('id')
        if not user_id:
            raise AuthenticationError('Invalid JWT: missing field id')
    except ExpiredSignatureError:
        raise TokenExpiredError('Token has expired')
    except InvalidTokenError as exc:
        raise AuthenticationError(f'Invalid token: {str(exc)}')
    return user_id

