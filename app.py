from flask import Flask, request
from flask_login import LoginManager
from models.user import User
from route.routes import init_routes
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_pyfile('.env')
login_manager = LoginManager(app)
bootstrap = Bootstrap(app)

@login_manager.user_loader
def current_user(user_id):
    return User.query.get(user_id)

@app.before_first_request
def create_db():
   db.create_all()

if __name__ == "__main__":
    from data.sql_alchemy import db
    db.init_app(app)
    init_routes(app)
    app.run(debug=True)
