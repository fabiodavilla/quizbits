import json
from app import db
from flask import Blueprint, make_response, render_template, request, session
from app.models.answer import Answer
from app.models.quiz import Quiz
from app.models.user import User
import os

data_controller = Blueprint('data', __name__, url_prefix='/data')


@data_controller.route('/', methods=['GET', 'POST'])
def data():
    return render_template("data.html")


@data_controller.route('/export', methods=['GET'])
def export_data():
    export = {}
    export['user'] = []
    export['quiz'] = []
    export['answer'] = []

    users = User.query.all()
    quizzes = Quiz.query.all()
    answers = Answer.query.all()

    for user in users:
        temp = user.to_dict()
        del temp['quiz']
        del temp['answer']
        export['user'].append(temp)

    for quiz in quizzes:
        temp = quiz.to_dict()
        del temp['answer']
        export['quiz'].append(temp)

    for answer in answers:
        temp = answer.to_dict()
        export['answer'].append(temp)

    path = os.path.join(os.sep, os.path.dirname(
        __file__), '..', '..', 'export.json')

    with open(path, "w") as outfile:
        json.dump(export, outfile, indent=4)

    if os.path.isfile(path):
        return make_response({ 'message': 'Success' }, 200)
    else:
        return make_response({ 'message': 'Failed' }, 500)


@data_controller.route('/import', methods=['POST'])
def import_data():
    file = request.files['file']

    db.session.execute('DELETE FROM answer')
    db.session.execute('DELETE FROM quiz')
    db.session.execute('DELETE FROM user')
    db.session.commit()

    content = json.loads(file.read())

    for user in content['user']:
        user = User(user['name'], user['email'], user['password'], user['status'])
        db.session.add(user)

    for quiz in content['quiz']:
        quiz = Quiz(quiz['name'], quiz['content'], quiz['user_id'], quiz['active'])
        db.session.add(quiz)

    for answer in content['answer']:
        answer = Answer(answer['content'], answer['user_id'], answer['quiz_id'])
        db.session.add(answer)

    db.session.commit()

    session.pop('email', None)
    
    return make_response({ 'message': 'Success' }, 200)
    