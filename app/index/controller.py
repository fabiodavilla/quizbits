from flask import Blueprint, render_template
from app.models.answer import Answer
from app.models.quiz import Quiz

from app.models.user import User

index_controller = Blueprint('index', __name__, url_prefix='/')


@index_controller.route('/', methods=['GET'])
def index():
    users = User.query.count()
    quizzes_active = Quiz.query.filter_by(active=True).count()
    quizzes_inactive = Quiz.query.filter_by(active=False).count()
    answers = Answer.query.count()

    return render_template("index.html", data=[users, quizzes_active + quizzes_inactive, quizzes_active, quizzes_inactive, answers])
