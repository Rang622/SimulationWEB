from flask import Blueprint, render_template

bp = Blueprint('learning', __name__, url_prefix='/learning')


@bp.route('/')
def learning():
    return render_template('First/learning.html')