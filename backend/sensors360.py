  
from app import app, db
from app.models import User, Sensor, Heartbeat


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Sensor': Sensor, 'Heartbeat': Heartbeat}