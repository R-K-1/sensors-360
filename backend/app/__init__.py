from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from flask_socketio import SocketIO, emit
#from flask_cors import CORS
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import server, models

"""
socketio = SocketIO(app)
CORS(app)

socketio.run(app, debug=True)
"""

#http_server = WSGIServer(('',5000), app, handler_class=WebSocketHandler)
#print("wsgi started")
#http_server.serve_forever()