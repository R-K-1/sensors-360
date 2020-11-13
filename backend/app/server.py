import sys
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.models import Heartbeat
from datetime import datetime

from config import Config
from app import app
app.config.from_object(Config)
db = SQLAlchemy(app)


@app.route('/api/v0/heartbeat', methods=['POST'])
def post_heartbit():
    print(request.args)
    return_value = "success"
    try:
        heartbeat = Heartbeat(sensor_id=int(request.args.get('sensor_id')),
                            timestamp=datetime.fromtimestamp(int(request.args.get('timestamp'))))
        db.session.add(heartbeat)
        db.session.commit()
    except IOError:
        print(sys.exc_info()[0])
        return_value = "IO Error"
    except ValueError:
        print(sys.exc_info()[0])
        return_value = "value error"
    except:
        print(sys.exc_info()[0])
        return_value = "unhandled error"
    
    return return_value

