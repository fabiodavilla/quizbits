import json
from flask import Blueprint, make_response, redirect, render_template, request, url_for
from ..models.user import User
from app import db
from datetime import datetime

user_controller = Blueprint('user', __name__, url_prefix='/user')


@user_controller.route('/', methods=['GET'])
def users():
    if request.method == 'GET':
        users = User.query.all()

        return render_template("list-users.html", users=users)


@user_controller.route('/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'GET':
        return render_template("create-user.html")
    else:
        data = request.form
        user = User(data['name'], data['email'], data['password'], 1)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('user.users'))


@user_controller.route('/<id>', methods=['GET', 'PUT', 'DELETE'])
def modify(id):
    user = User.query.filter_by(id=int(id)).first()

    if request.method == 'GET':
        return render_template("update-user.html", body=user)

    elif request.method == 'PUT':
        data = json.loads(request.get_data(
            parse_form_data=True).decode('utf-8'))

        if data['password'] == data['confirm-password']:
            user.name = data['name']
            user.password = data['password']
            user.updated_at = datetime.now()
            db.session.commit()
            return make_response({}, 200)
        else:
            return make_response({}, 500)
    else:
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response({}, 200)
        else:
            return make_response({}, 500)
