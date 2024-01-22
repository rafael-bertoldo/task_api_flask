from flask import jsonify, current_app, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.user_service import UserService


class UserController:
    @staticmethod
    def create_user():
        data = request.get_json()
        db = current_app.db
        # jwt_manager = current_app.jwt

        user_service = UserService()
        user, error_message = user_service.create_user(data, db)

        if error_message:
            return {"message": error_message}, 409

        user_dict = {
            'id': user.user_id,
            'name': user.user_name,
            'email': user.user_email
        }

        return jsonify(user_dict), 201
    

    @staticmethod
    @jwt_required()
    def get_profile():
        current_user = get_jwt_identity()
        user = UserService.get_profile(current_user)
        return jsonify(user), 200
    

    @staticmethod
    @jwt_required()
    def update_profile():
        data = request.get_json()
        db = current_app.db
        current_user = get_jwt_identity()
        user_service = UserService()

        user = user_service.update_profile(data, current_user, db)
        
        user_dict = {
            "id": user.user_id,
            "name": user.user_name,
            "email": user.user_email,
            
        }

        return jsonify(user_dict), 200
    

    @staticmethod
    @jwt_required()
    def delete_profile():
        db = current_app.db
        current_user = get_jwt_identity()
        user_service = UserService()

        deleted = user_service.delete_user(current_user, db)

        return jsonify({"message": deleted}), 200