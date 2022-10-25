from flask import Blueprint, render_template

about_controller = Blueprint('about', __name__, url_prefix='/about')

@about_controller.route('/', methods=['GET'])
def bout():
    return render_template("about.html", page_title="QuizBits - About page")