import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret!'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql+psycopg2://sensors360admin:saquyu-8BDNKT8pK@localhost/sensors360'
    SQLALCHEMY_TRACK_MODIFICATIONS = False