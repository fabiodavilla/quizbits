from flask import Blueprint, render_template

data_controller = Blueprint('data', __name__, url_prefix='/data')


@data_controller.route('/', methods=['GET', 'POST'])
def data():
    return render_template("data.html")
