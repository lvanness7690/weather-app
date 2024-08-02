from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    weather = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    humidity = db.Column(db.Integer, nullable=False)
    pressure = db.Column(db.Integer, nullable=False)
    wind_speed = db.Column(db.Float, nullable=False)
    sunrise = db.Column(db.String(50), nullable=False)
    sunset = db.Column(db.String(50), nullable=False)