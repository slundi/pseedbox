from flask import Flask, request
from pseedbox import babel
from config import LANGUAGES, SECRET_KEY

app = Flask(__name__, static_url_path = "", static_folder = "static")
app.secret_key = SECRET_KEY

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())
