from flask import Blueprint, request, render_template, redirect, url_for
from pybo.models import EnvironmentalData
from pybo import db

bp = Blueprint('setting', __name__, url_prefix='/setting')

@bp.route('/')
def setting():
    return render_template('First/setting.html')

@bp.route('/save', methods=['POST'])
def save_setting():
    new_data = EnvironmentalData(
        Time=bool(request.form.get('Time')),
        Humidity=request.form['Humidity'],
        Weather=request.form['Weather'],
        PreviousWeather=request.form['PreviousWeather'],
        Weight=request.form['Weight']
    )
    db.session.add(new_data)
    db.session.commit()
    return redirect(url_for('setting.setting'))