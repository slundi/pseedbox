from flask import Flask, request, g
from flask_socketio import SocketIO
import xmlrpc.client
import config


app = Flask(__name__, static_url_path = "", static_folder = "static")
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['MAX_CONTENT_LENGTH'] = config.MAX_UPLOAD_SIZE
socketio = SocketIO(app)
server=xmlrpc.client.ServerProxy(config.REMOTE_URL)
torrents = []

from . import views
from . import websockets
