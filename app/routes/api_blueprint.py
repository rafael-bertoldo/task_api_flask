from flask import Blueprint
from . import task_blueprint, user_blueprint, session_blueprint

bp = Blueprint('api_bp', __name__, url_prefix='/api')

bp.register_blueprint(user_blueprint.bp)
bp.register_blueprint(task_blueprint.bp)
bp.register_blueprint(session_blueprint.bp)
