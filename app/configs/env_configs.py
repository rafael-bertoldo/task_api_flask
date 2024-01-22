from flask import Flask
import os
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager


load_dotenv()


def init_app(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = bool(os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS'))
    app.config["JSON_SORT_KEYS"] = False
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 24 * 60 * 60
