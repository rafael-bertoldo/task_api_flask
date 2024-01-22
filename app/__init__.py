from flask import Flask
from app.configs import database, env_configs, migration
from app.routes import api_blueprint
from flask_jwt_extended import JWTManager



def create_app():
    app = Flask(__name__)

    env_configs.init_app(app)
    database.init_app(app)
    migration.init_app(app)
    app.register_blueprint(api_blueprint.bp)
    app.jwt = JWTManager(app)

    return app

