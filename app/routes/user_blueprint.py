from flask import Blueprint
from app.controllers.user_controller import UserController

bp = Blueprint('users_bp', __name__, url_prefix='/users')

bp.post('')(UserController.create_user)
bp.get('/profile')(UserController.get_profile)
bp.patch('/profile')(UserController.update_profile)
bp.delete('/profile')(UserController.delete_profile)