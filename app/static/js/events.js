socket.on('connection', function(socket){
    socket.on('system', function(data){ //update system info
        hdd=document.getElementById('hdd');
        cpu=document.getElementById('cpu');
        ram=document.getElementById('ram');
        //TODO: read data, change title attribute & update UI with blue-green-red gradient
    });
    socket.on('notify', function(data){
        //TODO: 
    });
    socket.on('log', function(data){ //update log
        //TODO: 
    });
    socket.on('torrents', function(data){ //update UI with torrent informations
        //TODO: 
    });
});
