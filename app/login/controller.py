from flask import Blueprint, render_template

login_controller = Blueprint('login', __name__, url_prefix='/login')

@login_controller.route('/', methods=['GET', 'POST'])
def login():
    return render_template("login.html", page_title="QuizBits - Login page")