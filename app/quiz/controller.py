import json
from flask import Blueprint, make_response, redirect, render_template, request, session, url_for
from app import db
from app.models.quiz import Quiz
from app.models.user import User

quiz_controller = Blueprint('quiz', __name__, url_prefix='/quiz')


@quiz_controller.route('/', methods=['GET', 'PUT'])
def list_quiz():
    quizzes = Quiz.query.all()

    return render_template("list-quiz.html", quizzes=quizzes)


@quiz_controller.route('/create', methods=['GET', 'POST'])
def create_quiz():
    if request.method == 'GET':
        return render_template("create-quiz.html")
    else:
        user = User.query.filter_by(email=session['email']).first()

        data = json.loads(request.get_data(
            parse_form_data=True).decode('utf-8'))

        if data['title'] != "" and len(data['questions']) > 0:
            quiz = Quiz(data['title'], json.dumps(data['questions']), user.id)
            db.session.add(quiz)
            db.session.commit()

            return make_response({}, 200)
        else:
            return make_response({}, 500)


@quiz_controller.route('/<id>', methods=['PUT'])
def update_quiz(id):
    quiz = Quiz.query.filter_by(id=int(id)).first()
    quiz.active = False
    db.session.commit()
    return redirect(url_for("quiz.list_quiz"))


@quiz_controller.route('/answer-list', methods=['GET'])
def answer_list_quiz():
    return render_template("answer-list-quiz.html")


@quiz_controller.route('/answer/<id>', methods=['GET'])
def answer_quiz(id):
    return render_template("answer.html")


@quiz_controller.route('/results', methods=['GET'])
def results_quiz():
    return render_template("results.html")
