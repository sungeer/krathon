import hashlib
import json
import uuid
from datetime import datetime, date
from decimal import Decimal

from flask import Response
from werkzeug.http import HTTP_STATUS_CODES
from werkzeug.exceptions import default_exceptions


class BaseResponse:

    def __init__(self):
        self.status = True
        self.error_code = None
        self.message = None
        self.data = None

    def to_dict(self):
        resp_dict = {
            'status': self.status,
            'error_code': self.error_code,
            'message': self.message,
            'data': self.data
        }
        return resp_dict


class JsonExtendEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, (tuple, list, datetime)):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, bytes):
            return obj.decode('utf-8')
        return super().default(obj)


class JsonExtendResponse(Response):

    def __init__(self, response, **kwargs):
        json_response = json.dumps(response, cls=JsonExtendEncoder, ensure_ascii=False).encode('utf-8')
        super().__init__(json_response, mimetype='application/json', **kwargs)


def jsonify(*args, **kwargs):
    if args and kwargs:
        raise TypeError('jsonify() behavior undefined when passed both args and kwargs')
    elif len(args) == 1:
        content = args[0]
    else:
        content = args or kwargs
    response = BaseResponse()
    response.data = content
    response = response.to_dict()
    return JsonExtendResponse(response)


def jsonify_exc(error_code, message=None):
    if not message:
        message = HTTP_STATUS_CODES.get(error_code)
    response = BaseResponse()
    response.status = False
    response.error_code = error_code
    response.message = message
    response = response.to_dict()
    return JsonExtendResponse(response)


def abort(error_code, message=None):
    exception_type = default_exceptions.get(error_code)  # NotFound
    raise exception_type(description=message)


def dict_to_json(data):
    if not data:
        data = {}
    return json.dumps(data, cls=JsonExtendEncoder, ensure_ascii=False)


def json_to_dict(json_data):
    return json.loads(json_data)


def generate_uuid():
    random_uuid = str(uuid.uuid4())
    md5 = hashlib.md5()
    md5.update(random_uuid.encode('utf-8'))
    return md5.hexdigest().lower()


def current_time():
    return datetime.now()
