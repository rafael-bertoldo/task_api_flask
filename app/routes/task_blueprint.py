from flask import Blueprint

bp = Blueprint('tasks_bp', __name__, url_prefix='/tasks')