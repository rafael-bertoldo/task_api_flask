from app.models.user_model import User
from sqlalchemy.exc import IntegrityError, NoResultFound
from flask_bcrypt import Bcrypt


class UserService:
    @staticmethod
    def create_user(data, db):
        bcrypt = Bcrypt()

        try:
            user = User(**data)
            user.user_password = bcrypt.generate_password_hash(
                data.get("user_password")
            ).decode("utf-8")

            db.session.add(user)
            db.session.commit()

            return user, None
        except IntegrityError:
            return None, "Email already exists"

    @staticmethod
    def get_profile(id):
        try:
            user = User.query.filter_by(user_id=id).one()

            output = {
                "user_email": user.user_email,
                "user_id": user.user_id,
                "user_name": user.user_name,
            }
            return output
        except NoResultFound:
            return "User not found"

    @staticmethod
    def update_profile(data, id, db):
        bcrypt = Bcrypt()

        try:
            user_by_email = User.query.filter_by(user_email=data["user_email"]).one
        except IntegrityError:
            return "Email already exists"

        try:
            user = User.query.get(id)

            if user:
                user.user_name = data.get("user_name", user.user_name)
                user.user_email = data.get("user_email", user.user_email)

                hash_pass = bcrypt.generate_password_hash(
                    data.get("user_password")
                ).decode("utf-8")
                user.user_password = hash_pass

                db.session.commit()

                return user
        except NoResultFound:
            return "User not found"

    @staticmethod
    def delete_user(id, db):
        try:
            user = User.query.get(id)

            if user:
                db.session.delete(user)
                db.session.commit()
                return "Usuário deletado com sucesso"
            else:
                return "Usuário não encontrado"
        except IntegrityError:
            db.session.rollback()
            return "Erro ao deletar usuário"
