from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)
# create tables
from app.models.user import User

# controllers
from app.index.controller import index_controller
from app.login.controller import login_controller
from app.users.controller import user_controller
from app.quiz.controller import quiz_controller
from app.about.controller import about_controller
from app.data.controller import data_controller

# Register blueprint
app.register_blueprint(index_controller)
app.register_blueprint(login_controller)
app.register_blueprint(user_controller)
app.register_blueprint(quiz_controller)
app.register_blueprint(about_controller)
app.register_blueprint(data_controller)

with app.app_context():
    db.create_all()
