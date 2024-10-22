from flask import Blueprint

from krathon.utils.tools import jsonify
from krathon.tasks.async_tasks import long_task

route = Blueprint('chat', __name__)


@route.post('/')
def index():
    long_task.long_running_task()
    message = {'message': 'Long-running task has been started!'}
    return jsonify(message)
