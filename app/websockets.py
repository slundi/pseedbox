from app import socketio, server, torrents, config, app
from flask_socketio import send, emit
from MediaInfo import MediaInfo
from app.models import *
from flask_apscheduler import APScheduler
import json

#https://docs.python.org/3/library/xmlrpc.client.html
#https://rtorrent-docs.readthedocs.io/en/latest/cmd-ref.html

### Crons ###
scheduler = APScheduler()
scheduler.init_app(app)
#scheduler.start()
#scheduler.add_job(refresh_torrents, trigger="interval", seconds=config.TORRENT_LIST_REFRESH_TIME)
#scheduler.add_job(refresh_speeds, trigger="interval", seconds=config.SPEEDS_REFRESH_TIME)

#@scheduler.task('interval', id='refresh_speeds', seconds=config.SPEEDS_REFRESH_TIME, misfire_grace_time=300)
def refresh_speeds():
    print('WS: sending speeds')
    data=server.d.multicall2('', ('default', 'd.hash=', 'd.size_chunks=', 'd.chunk_size=', 'd.completed_chunks=', \
                                'd.down.total=', 'd.down.rate=', 'd.up.total=', 'd.up.rate=', 'd.ratio='))
    emit('t:speeds', json.dumps(data), broadcast=True)

#@scheduler.task('interval', id='refresh_torrents', seconds=config.TORRENT_LIST_REFRESH_TIME, misfire_grace_time=300)
def refresh_torrents():
    print('WS: torrent list')
    data=server.d.multicall2('', ('default', 'd.hash=', 'd.get_directory=', 'd.get_name=', \
                                'd.size_bytes=', 'd.size_chunks=', 'd.chunk_size=', 'd.completed_chunks=', \
                                'd.is_multi_file=', 'd.is_private=', 'd.priority=','d.ratio='))
    torrents.clear()
    for d in data:
        t=Torrent(d[0])
        t.name = d[2]
        t.size = d[3]
        t.path = d[1]
        t.chunks = d[4]
        t.chunk_size = d[5]
        t.completed_chunks = d[6]
        t.multiple_files = d[7]==1
        t.private = d[8]==1
        t.proiority = d[9]
        t.ratio = d[10]
        torrents.append(t)
    #print(json.dumps(torrents))
    emit('t:list', json.dumps([t.__dict__ for t in torrents]), broadcast=True)
    refresh_speeds()

### User ###
@socketio.on('connect')
def user_connected():
    print('User connected')
    #TODO: send torrent list
    #for h in server.download_list('', ('default')):
    #    print(h,server.d.get_name(h),'\t',server.d.get_directory(h),server.d.get_free_diskspace(h))
    #    break
    refresh_torrents()
#@socketio.on('disconnect')
#def user_disconnected():
#    print('User disconnected')

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
    emit('f:priority', [torrent, file, priority], broadcast=True)

@socketio.on('media_info')
def media_info(torrent, file):
    print('media_info')
    emit('f:media_info', [torrent, file, Mediainfo(filename = server.d.get_directory(torrent)+'/'+server.f.get_path(torrent,file)).getInfo()])

### Server commands ###

### Peers commands ###

### Tracker commands ###


