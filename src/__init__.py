from flask import Flask, request
from flask_login import LoginManager
from models.user import User
from route.routes import init_routes
from flask_bootstrap import Bootstrap
from src.sql_alchemy import db

login_manager = LoginManager()
bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('.env')
    login_manager.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)

    from route import routes
    routes.init_routes(app)

    @login_manager.user_loader
    def current_user(user_id):
        return User.query.get(user_id)

    @app.before_first_request
    def create_db():
        db.create_all()

    return app