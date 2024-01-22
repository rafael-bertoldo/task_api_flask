from flask import Flask
from flask_migrate import Migrate

def init_app(app: Flask):

  from app.models.user_model import User
  from app.models.task_model import Task

  Migrate(app, app.db)