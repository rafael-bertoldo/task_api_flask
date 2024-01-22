from flask import jsonify, current_app, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.task_service import TaskService
from sqlalchemy.exc import NoResultFound


class TaskController:
    @staticmethod
    @jwt_required()
    def create_task():
        current_user = get_jwt_identity()
        data = request.get_json()
        db = current_app.db
        task_service = TaskService

        task = task_service.create_task(data, current_user, db)

        return jsonify(task), 201

    @staticmethod
    @jwt_required()
    def read_all():
        current_user = get_jwt_identity()
        task_service = TaskService

        tasks = task_service.read_all_tasks(current_user)

        return jsonify(tasks)

    @staticmethod
    @jwt_required()
    def read_by_id(task_id):
        current_user = get_jwt_identity()
        task_service = TaskService
        try:
            task = task_service.read_by_id(current_user, task_id)

            return jsonify(task)
        except NoResultFound:
            return {"Message": "Task not found"}, 404
        

    @staticmethod
    @jwt_required()
    def update_by_id(task_id):
        current_user = get_jwt_identity()
        task_service = TaskService
        data = request.get_json()
        db = current_app.db

        try:
            task = task_service.update_task(data, current_user, task_id, db)

            return jsonify(task), 200
        except NoResultFound as e:
            return {"Message": "Task not found"}, 404
        

    @staticmethod
    @jwt_required()
    def delete_by_id(task_id):
        current_user = get_jwt_identity()
        task_service = TaskService()
        db = current_app.db

        try:
            task = task_service.delete_task(current_user, task_id, db)

            return jsonify({"message": task}), 200
        except NoResultFound:
            return {"Message": "Task not found"}, 404
