from flask import Blueprint, render_template

index_controller = Blueprint('index', __name__, url_prefix='/')

@index_controller.route('/', methods=['GET'])
def index():
    return render_template("index.html", page_title="QuizBits - Index page")