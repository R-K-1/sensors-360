from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import time
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.id, self.username)

class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(64), index=True, unique=True)
    heartbeats = db.relationship('Heartbeat', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Sensor {}>'.format(self.id, self.tag)

class Heartbeat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'))
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return '<Heartbeat {}>'.format(self.id, self.sensor_id, self.timestamp)

db.create_all()

for i in range(20):
    sensor = Sensor(id=i, tag=f'Sensor {i}')
    db.session.add(sensor)

for i in range(20):
    heartbeat = Heartbeat(sensor_id=i, timestamp=datetime.utcnow())
    db.session.add(heartbeat)

db.session.commit()
