import json
from click import Path
from flask import Blueprint, render_template
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

    return "Success"


@data_controller.route('/import', methods=['GET'])
def import_data():
    path = os.path.join(os.sep, os.path.dirname(
        __file__), '..', '..', 'export.json')

    if os.path.isfile(path):
        with open(path, "w") as outfile:
            json.dump(export, outfile, indent=4)
    else:
        return 'File not found'
