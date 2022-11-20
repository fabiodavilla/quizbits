import json
from flask import Blueprint, make_response, redirect, render_template, request, session, url_for
from app import db
from app.models.answer import Answer
from app.models.quiz import Quiz
from app.models.user import User

quiz_controller = Blueprint('quiz', __name__, url_prefix='/quiz')


@quiz_controller.route('/', methods=['GET', 'PUT'])
def list_quiz():
    user = User.query.filter_by(email=session['email']).first()
    quizzes = Quiz.query.filter_by(user_id=user.id).all()

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
            quiz = Quiz(data['title'], json.dumps(data['questions']), user.id, True)
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


@quiz_controller.route('/answer-list', methods=['GET', 'POST'])
def answer_list_quiz():
    user = User.query.filter_by(email=session['email']).first()
    quizzes = Quiz.query.filter(Quiz.user_id != user.id, Quiz.active == True).all()
    return render_template("answer-list-quiz.html", quizzes=quizzes)


@quiz_controller.route('/answer/<id>', methods=['GET', 'POST'])
def answer_quiz(id):
    if request.method == 'GET':
        quiz = Quiz.query.filter_by(id=int(id)).first()
        contentJson = json.loads(quiz.content)
        content = [(i, contentJson[i]) for i in contentJson]

        return render_template("answer.html", quiz=quiz, content=content)
    else:
        user = User.query.filter_by(email=session['email']).first()
        data = json.dumps(request.form)

        if data and user:
            answer = Answer(data, user.id, int(id))
            db.session.add(answer)
            db.session.commit()

        return redirect(url_for("quiz.answer_list_quiz"))


@quiz_controller.route('/results', methods=['GET'])
def results_quiz():
    answered = Quiz.query.filter_by(active=False).all()

    return render_template("result-list.html", list=answered)

@quiz_controller.route('/results/<id>', methods=['GET'])
def results_list(id):
    answers = Answer.query.filter_by(quiz_id=id).all()
    quiz = Quiz.query.filter_by(id=id).first()

    answersList = []
    for answer in answers:
        user = User.query.filter_by(id=answer.user_id).first()

        newObj = {}
        newObj['id'] = answer.id
        newObj['created_at'] = answer.created_at
        newObj['user'] = user.name
        newObj['content'] = []

        quizContent = json.loads(quiz.content)
        answerContent = json.loads(answer.content)
        for question in quizContent:
            newObj['content'].append((quizContent[question], answerContent[question]))

        answersList.append(newObj)
    
    return render_template("result.html", quiz=quiz.name, list=answersList)
