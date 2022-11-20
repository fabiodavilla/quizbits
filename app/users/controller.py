import json
from flask import Blueprint, make_response, redirect, render_template, request, session, url_for
from ..models.user import User
from app import db
from datetime import datetime

user_controller = Blueprint('user', __name__, url_prefix='/user')


@user_controller.route('/', methods=['GET'])
def users():
    if request.method == 'GET':
        users = User.query.all()
        logged_user = User.query.filter_by(email=session['email']).first()

        return render_template("list-users.html", users=users, logged_user=logged_user)


@user_controller.route('/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'GET':
        return render_template("create-user.html")
    else:
        status = User.query.count()

        data = request.form
        user = User(data['name'], data['email'],
                    data['password'], True if status == 0 else False)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('user.users'))


@user_controller.route('/<id>', methods=['GET', 'PUT', 'DELETE'])
def modify(id):
    user = User.query.filter_by(id=int(id)).first()
    logged_user = User.query.filter_by(email=session['email']).first()

    if request.method == 'GET':
        return render_template("update-user.html", body=user, logged_user=logged_user)

    elif request.method == 'PUT':
        data = json.loads(request.get_data(
            parse_form_data=True).decode('utf-8'))

        if data['password'] == data['confirm-password']:
            user.name = data['name'] if data['name'] != '' else user.name
            user.password = data['password'] if data['password'] != '' else user.password
            user.status = True if "status" in data else False
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
