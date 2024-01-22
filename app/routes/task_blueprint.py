from flask import Blueprint
from app.controllers.task_controllers import TaskController

bp = Blueprint('tasks_bp', __name__, url_prefix='/tasks')
bp.post('')(TaskController.create_task)
bp.get('')(TaskController.read_all)
bp.get('/<task_id>')(TaskController.read_by_id)
bp.patch('/<task_id>')(TaskController.update_by_id)
bp.delete('/<task_id>')(TaskController.delete_by_id)