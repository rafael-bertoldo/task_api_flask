from app.models.task_model import Task
from sqlalchemy.exc import IntegrityError, NoResultFound

class TaskService:
    @staticmethod
    def create_task(data, id, db):
        try:
            new_task = {
                **data,
                "user_id": id
            }
            print(new_task)
            task = Task(**new_task)

            db.session.add(task)
            db.session.commit()

            return task
        except IntegrityError:
            db.rollback()
            return 'Pelase verify the task fields and try again'
        
    @staticmethod
    def read_all_tasks(id):
        try:
            tasks = Task.query.filter_by(user_id=id).all()

            return tasks
        except IntegrityError:
            return 'An error occured, please try again'
        

    @staticmethod
    def read_by_id(user_id, task_id):
        try:
            task = Task.query.filter_by(user_id=user_id, task_id=task_id).one_or_none()

            if task is None:
                raise NoResultFound('Task not found')

            return task
        except NoResultFound:
            raise


    @staticmethod
    def update_task(data, user_id, task_id, db):
        try:
            task = Task.query.filter_by(user_id=user_id, task_id=task_id).one_or_none()

            if task:
            
                task.task_content = data.get("task_content", task.task_content)

                db.session.commit()

                return {"message": "Task update successfully"}
            else:
                raise NoResultFound("Task not found")
        except IntegrityError:
            return "Error updating task"


    @staticmethod
    def delete_task(user_id, task_id, db):
        try:
            task = Task.query.filter_by(user_id=user_id, task_id=task_id).one_or_none()

            if task:
                db.session.delete(task)
                db.session.commit()
                return "Task delete succsessfully"
            else:
                raise NoResultFound("Task not found")
        except IntegrityError:
            return "Error deleting Task"