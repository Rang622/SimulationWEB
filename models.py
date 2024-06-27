from flask_sqlalchemy import SQLAlchemy
from pybo import db
import enum
from sqlalchemy import Column, Integer, Float, String, Enum

class WeatherStatus(enum.Enum):
    Windy = 'Windy'
    Rainy = 'Rainy'
    WNone = 'None'

class EnvironmentalData(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	Time = db.Column(db.Float, nullable=False)
	Humidity = db.Column(db.Float, nullable=False)
	Weather = db.Column(Enum(WeatherStatus), nullable=False)
	PreviousWeather = db.Column(db.Boolean, nullable=False)
	Weight = db.Column(db.Float, nullable=False)