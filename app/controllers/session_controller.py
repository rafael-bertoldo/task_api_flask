from flask import jsonify, request, current_app
from app.services.session_service import SessionService


class SessionController:

    @staticmethod
    def login():
        data = request.get_json()
        db = current_app.db
        jwt_manager = current_app.jwt

        session_service = SessionService(jwt_manager)
        user = session_service.login(data, db)

        if user:
            access_token = session_service.generate_token(user)
            return jsonify({"access_token": access_token}), 200
        else:
            return jsonify({"message": "Invalid credential"}), 401
