from krathon.utils.tools import jsonify
from krathon.tasks.async_tasks import long_task


def index():
    long_task.long_running_task()
    message = {'message': 'Long-running task has been started!'}
    return jsonify(message)
