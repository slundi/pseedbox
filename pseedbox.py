from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_babel import Babel
import os
import config

app = Flask(__name__, static_url_path = "", static_folder = "static")
app.config['SECRET_KEY'] = config.SECRET_KEY
babel = Babel(app)
socketio = SocketIO(app)

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    socketio.run(app, host = HOST, port = config.SERVER_PORT)
