from flask import Blueprint, render_template

user_controller = Blueprint('user', __name__, url_prefix='/user')

@user_controller.route('/', methods=['GET'])
def users():
    return render_template("list-users.html")

@user_controller.route('/create', methods=['GET'])
def create_user():
    return render_template("create-user.html")