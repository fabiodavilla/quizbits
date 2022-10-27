from flask import Blueprint, render_template

quiz_controller = Blueprint('quiz', __name__, url_prefix='/quiz')

@quiz_controller.route('/', methods=['GET'])
def list_quiz():
    return render_template("list-quiz.html")

@quiz_controller.route('/create', methods=['GET'])
def create_quiz():
    return render_template("create-quiz.html")

@quiz_controller.route('/answer-list', methods=['GET'])
def answer_list_quiz():
    return render_template("answer-list-quiz.html")

@quiz_controller.route('/answer/<id>', methods=['GET'])
def answer_quiz(id):
    return render_template("answer.html")

@quiz_controller.route('/results', methods=['GET'])
def results_quiz():
    return render_template("results.html")