from flask import request

from krathon.models.user_model import UserModel
from krathon.utils.tools import jsonify, abort
from krathon.utils import jwt_util
from krathon.utils.schemas import access_token_schema
from krathon.utils.decorators import validate_request


@validate_request(access_token_schema)
def get_access_token():
    body = request.json
    phone_number = body['phone_number']
    password = body['password']

    db_user = UserModel().get_user_by_phone(phone_number)
    if not db_user:
        return abort(404, 'User not found')

    db_password = db_user['password_hash']
    is_pwd = jwt_util.validate_password(password, db_password)
    if not is_pwd:
        return abort(403, 'Incorrect password')

    access_token = jwt_util.generate_token({'id': db_user['id']})
    jwt_token = {'access_token': access_token, 'token_type': 'bearer'}
    return jsonify(jwt_token)
