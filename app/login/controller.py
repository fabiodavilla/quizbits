from flask import Blueprint, redirect, render_template, request, session, url_for
from ..models.user import User

login_controller = Blueprint('login', __name__, url_prefix='/auth')

@login_controller.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        print(session)
        return render_template("login.html")
    else:
        data = request.form

        if (not data['email'] and not data['password']):
            return render_template("login.html", error=f"Insert the required informations!")

        user = User.query.filter_by(email=data['email']).first()

        if (not user):
            return render_template("login.html", error=f"Email {data['email']} not found!")

        if (user.password != data['password']):
            return render_template("login.html", error=f"Password doesn't Match")

        if (user.password == data['password']):
            session['email'] = request.form['email']
            return redirect(url_for('index.index'))

        return 'User not found'

@login_controller.route('/logout', methods=['GET'])
def logout():
    session.pop('email', None)
    return redirect(url_for('login.login'))
