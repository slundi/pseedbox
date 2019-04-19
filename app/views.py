from flask import request, session, render_template, redirect, url_for, make_response, send_from_directory, abort
from flask_socketio import send, emit
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

@app.route('/admin')
@auth.login_required
def admin():
    return render_template('admin.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('user', None)
    #redirect to error 401 to logout from basic auth
    abort(401)
    return redirect('/', code=401)

@app.errorhandler(401)
def error_401_unauthorized(error):
    print("401")
    return render_template('logout.html'), 401

@socketio.on('send_torrent')
def send_torrent(torrent, category, start = True):
    print('send_torrent')
@socketio.on('remove_torrent')
def remove_torrent(torrent):
    print('remove_torrent')
@socketio.on('check_torrent')
def check_torrent(torrent):
    print('check_torrent')
@socketio.on('download_torrent')
def download_torrent(torrent):
    print('download_torrent')
@socketio.on('edit_torrent')
def edit_torrent(torrent,tracker,info,private):
    print('edit_torrent')
@socketio.on('retracker')
def retracker(torrent,tracker):
    print('retracker')
@socketio.on('create_torrent')
def create_torrent(path, trackers, infos, source, chunk_size, seed=True, private_tracker=False):
    print('create_torrent')

@socketio.on('start_torrent')
def start_torrent(torrent):
    print('start_torrent')
@socketio.on('pause_torrent')
def pause_torrent(torrent):
    print('pause_torrent')
@socketio.on('stop_torrent')
def stop_torrent(torrent):
    print('stop_torrent')

@socketio.on('set_priority')
def set_priority(torrent, priority=2): #priority from 0 to 3
    print('set_priority')
@socketio.on('set_ratio')
def set_ratio(torrent, ratio):
    print('set_ratio',ratio)
@socketio.on('set_speed')
def set_speed(torrent):
    print('set_speed')
#@socketio.on('sort_torrent')
#def sort_torrent(torrent):
#    print('sort_torrent')
@socketio.on('set_file_priority')
def set_file_priority(torrent, file, priority):
    print('set_file_priority')
@socketio.on('limit_download')
def limit_download(v):
    print('limit_download',v)
@socketio.on('limit_upload')
def limit_upload(v):
    print('limit_upload',v)