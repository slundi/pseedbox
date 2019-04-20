from app import socketio, server
from flask_socketio import send, emit

### Torrent commands ###
@socketio.on('send_torrent')
def send_torrent(torrent, category, start = True):
    print('send_torrent')
@socketio.on('remove_torrent')
def remove_torrent(torrent):
    print('remove_torrent')
    emit('t:remove', torrent, broadcast=True)
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
    server.d.start(torrent)
    emit('t:status', [torrent, 'started'], broadcast=True)
@socketio.on('pause_torrent')
def pause_torrent(torrent):
    print('pause_torrent')
    server.d.pause(torrent)
    emit('t:status', [torrent, 'paused'], broadcast=True)
@socketio.on('stop_torrent')
def stop_torrent(torrent):
    print('stop_torrent')
    server.d.stop(torrent)
    emit('t:status', [torrent, 'stopped'], broadcast=True)

@socketio.on('set_priority')
def set_priority(torrent, priority=2): #priority from 0 to 3
    print('set_priority')
    server.d.priority.set(torrent, priority)
    emit('t:priority', [torrent, priority], broadcast=True)
@socketio.on('set_ratio')
def set_ratio(torrent, ratio):
    print('set_ratio',ratio)
@socketio.on('set_speed')
def set_speed(torrent):
    print('set_speed')
#@socketio.on('sort_torrent')
#def sort_torrent(torrent):
#    print('sort_torrent')

@socketio.on('limit_download')
def limit_download(v):
    print('limit_download',v)
@socketio.on('limit_upload')
def limit_upload(v):
    print('limit_upload',v)

### File commands ###
@socketio.on('set_file_priority')
def set_file_priority(torrent, file, priority):
    print('set_file_priority')
    server.f.priority.set(file, priority)
    server.d.update_priorities()
    emit('f:priority', [torrent, priority], broadcast=True)

### Server commands ###

### Peers commands ###

### Tracker commands ###


