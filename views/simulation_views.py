from flask import Blueprint, render_template

bp = Blueprint('simulation', __name__, url_prefix='/simulation')


@bp.route('/')
def simulation():
    return render_template('First/simulation.html')