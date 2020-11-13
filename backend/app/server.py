from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.models import User, Sensor, Heartbeat

from config import Config

from app import app

@app.route('/api/v0/heartbeat', methods=['POST'])
def post_heartbit():
    print('posting heartbeat')
    return ''

