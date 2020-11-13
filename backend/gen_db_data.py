from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import time
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

for i in range(20):
    sensor = Sensor(id=i, tag=f'Sensor {i}')
    db.session.add(sensor)

for i in range(20):
    heartbeat = Heartbeat(sensor_id=i, timestamp=datetime.utcnow())
    db.session.add(heartbeat)

db.session.commit()
