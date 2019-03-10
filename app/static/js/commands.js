var socket = undefined;
function connect(url) {socket = io.connect(url);}

function send_torrent(torrent, category, start = true) {
    if(document.getElementById('torrent_file').value != "" && document.getElementById('add_category').value != "") {
        socket.on('connect', function() {
            //TODO:
            socket.emit('upload_torrent', {data: 'TODO: upload torrent', category: category, start: start});
        });
    }
}
function remove_torrent(t) { socket.emit('remove_torrent', {torrent: t}); }
function check_torrent(t) { socket.emit('check_torrent', {torrent: t}); }

function download_torrent(t) { socket.emit('download_torrent', {torrent: t}); }

function edit_torrent(t, url, i, p) { socket.emit('download_torrent', {torrent: t, tracker: url, info: i, priv: p}); }

function start_torrent(t) { socket.emit('start_torrent', {torrent: t}); }
function pause_torrent(t) { socket.emit('pause_torrent', {torrent: t}); }
function stop_torrent(t) { socket.emit('stop_torrent', {torrent: t}); }

function set_priority(t, priority=2) {/* Priority from 0 to 3 */}
function set_ratio(t, ratio = 1) { socket.emit('set_ratio', {torrent: t, ratio: ratio}); }
function set_speed(t, download = undefined, upload = undefined) { socket.emit('set_speed', {torrent: t, download: download, upload: upload}); }

function sort_torrent(t, category) { socket.emit('sort_torrent', {torrent: t, category: category}); }

function set_file_priority(t, file, priority) { socket.emit('set_file_priority', {torrent: t, file: f, priority: priority}); }

function label_torrent(t) {}
function create_torrent(path, trackers, infos, source, chunk_size, seed=true, private_tracker=false) {}
function limit_download(v) {}
function limit_upload(v) {}
function retracker(t, trackers) {}

function update_system_infos(data) {
    hdd=document.getElementById('hdd');
    cpu=document.getElementById('cpu');
    ram=document.getElementById('ram');
    //TODO: read data, change title attribute & update UI with blue-green-red gradient
}

function notify(){}

function update_log(data) {}