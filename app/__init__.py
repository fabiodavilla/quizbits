from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure
app.config.from_object('config')

# Secret key for session
app.secret_key = 'McQfTjWnZr4u7x!A%C*F-JaNdRgUkXp2'

db = SQLAlchemy(app)
# create tables
from app.models.user import User
from app.models.quiz import Quiz
from app.models.answer import Answer

# controllers
from app.index.controller import index_controller
from app.login.controller import login_controller
from app.users.controller import user_controller
from app.quiz.controller import quiz_controller
from app.about.controller import about_controller
from app.data.controller import data_controller
from app.error.controller import error_controller

# Register blueprint
app.register_blueprint(index_controller)
app.register_blueprint(login_controller)
app.register_blueprint(user_controller)
app.register_blueprint(quiz_controller)
app.register_blueprint(about_controller)
app.register_blueprint(data_controller)
app.register_blueprint(error_controller)

with app.app_context():
    db.create_all()

def render_login_button():
    return True if session.get('email') else False

def check_route(route):
    response = False
    routes = ['/data', '/user/create']

    if route[-1] == '/':
        route = route[:-1]

    for i in routes:
        if i == route:
            response = True

    return response

app.jinja_env.globals.update(render_login_button=render_login_button)
app.jinja_env.globals.update(check_route=check_route)