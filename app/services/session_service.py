from app.models.user_model import User
from sqlalchemy.exc import IntegrityError
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, JWTManager


class SessionService:
    def __init__(self, jwt_manager: JWTManager):
        self.jwt_manager = jwt_manager

    @staticmethod
    def login(data, db):

        user = User.query.filter_by(user_email=data['email']).first()

        if user and Bcrypt().check_password_hash(user.user_password, data['password']):
            return user
        else:
            return None

    @staticmethod
    def generate_token(user):
        access_token = create_access_token(identity=str(user.user_id))
        return access_token
