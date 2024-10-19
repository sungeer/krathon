from functools import wraps

from flask import request, g

from krathon.utils.tools import abort
from krathon.utils import jwt_util
from krathon.utils.schemas import User, validate_data
from krathon.models.user_model import UserModel


def auth_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        user_id, _ = jwt_util.verify_token(request)
        db_user = UserModel().get_user_by_id(user_id)
        if not db_user:
            return abort(401)
        g.user = User(**db_user)
        return func(*args, **kwargs)

    return decorated_function


def validate_request(schema):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            data = request.json
            validate_data(data, schema)
            return func(*args, **kwargs)

        return decorated_function

    return decorator


def permission_required(permission_name):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            perm = g.has_perm
            if perm not in (permission_name,):
                return abort(403)
            return func(*args, **kwargs)

        return decorated_function

    return decorator


def admin_required(func):  # @admin_required
    return permission_required('admin')(func)
