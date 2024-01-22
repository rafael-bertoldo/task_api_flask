from flask import Blueprint
from app.controllers.user_controller import UserController
from app.controllers.session_controller import SessionController

bp = Blueprint('session_bp', __name__, url_prefix='/login')

bp.post('')(SessionController.login)
