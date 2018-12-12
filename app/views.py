from flask import request, session, render_template, redirect, url_for, make_response, send_from_directory
from app import app, socketio
import app.modules.database as db
from app.modules import strings
import config
import time, hashlib

### Start of auth section
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
@auth.hash_password
def hash_pw(password):
    print('hash_pw',password)
    return hashlib.md5(password).hexdigest()

@auth.verify_password
def verify_password(username, password):
    h=hashlib.md5()
    h.update(password.encode('UTF-8'))
    user = db.get_user(username, h.hexdigest())
    if not user:
        return False
    session['username'] = user.username
    return True
### End of auth section
#print('views.py')

@app.route('/')
@auth.login_required
def index():
    #return 'Logged in as %s' % escape(session['username'])
    print('Logged user is', session['username'])
    return render_template('layout.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    #TODO: redirect to error 401 to logout from basic auth
    session.pop('user', None)
    return render_template('logout.html')

