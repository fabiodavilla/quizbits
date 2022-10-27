from flask import Blueprint, render_template

error_controller = Blueprint('error', __name__, url_prefix='/error')

@error_controller.route('/', methods=['GET'])
def error():
    return render_template("error.html")