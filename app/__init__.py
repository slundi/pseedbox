from flask import Flask, request, g
from flask_babel import Babel
from flask_socketio import SocketIO
import config


app = Flask(__name__, static_url_path = "", static_folder = "static")
app.config['SECRET_KEY'] = config.SECRET_KEY
babel = Babel(app)
socketio = SocketIO(app)

#i18n & l10n
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(config.LANGUAGES.keys())

@babel.timezoneselector
def get_timezone():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone

from . import views
