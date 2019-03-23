from flask import Flask, request, g
from flask_babel import Babel
from flask_socketio import SocketIO
import config


app = Flask(__name__, static_url_path = "", static_folder = "static")
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['MAX_CONTENT_LENGTH'] = config.MAX_UPLOAD_SIZE
babel = Babel(app)
socketio = SocketIO(app)

# Start of i18n & l10n section
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(config.LANGUAGES.keys())

@babel.timezoneselector
def get_timezone():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone
### End of i18n & l10n section

from . import views
