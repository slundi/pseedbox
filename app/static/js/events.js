//utility functions
function formatBytes(a,b){if(0==a)return"0 Bytes";var c=1024,d=b||2,e=["B","KB","MB","GB","TB","PB","EB","ZB","YB"],f=Math.floor(Math.log(a)/Math.log(c));return parseFloat((a/Math.pow(c,f)).toFixed(d))+" "+e[f]}
function dynamicSort(property) {
    var sortOrder = 1;
    if(property[0] === "-") {
        sortOrder = -1;
        property = property.substr(1);
    }
    return function (a,b) {
        var result = (a[property] < b[property]) ? -1 : (a[property] > b[property]) ? 1 : 0;
        return result * sortOrder;
    }
}

var torrents = [];
//events
socket.on('connection', function(socket){
    
});
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
socket.on('t:list', function(data){ //update UI with torrent informations
    //TODO: 
    console.log('Torrent list received:');
    tbody=document.getElementById('torrent_list');
    html = '';
    torrents = JSON.parse(data);
    torrents.sort(dynamicSort("name"));
    torrents.forEach(function(t){
        html+='<tr id="'+t.id+'">';
        html+='<td>'+t.name+'</td>';
        html+='<td>'+formatBytes(t.size)+'</td>';
        html+='<td>%'+'</td>';
        html+='<td>D'+'</td>';
        html+='<td>DS'+'</td>';
        html+='<td>ETA'+'</td>';
        html+='<td>U'+'</td>';
        html+='<td>US'+'</td>';
        html+='<td>'+t.ratio+'</td>';
        html+='<td>MR'+'</td>';
        html+='<td>DR'+'</td>';
        html+='<td>added'+'</td>';
        html+='<td>'+t.owner+'</td>';
        html+='<td>S'+'</td>';
        html+='<td>C'+'</td>';
        html+='</tr>';
    });
    tbody.innerHTML=html;
});

socket.on('t:speeds', function(data){
    speeds=JSON.parse(data);
    console.log(torrents);
    for(i=0;i<speeds.length;i++){
        let t=torrents.find(x => x.id==speeds[i][0]);
        var e=document.getElementById(t.id);
        e.childNodes[2].innerHTML = Math.round(100 * speeds[i][3] / speeds[i][1]) + ' %';
        e.childNodes[3].innerHTML = (speeds[i][4]==0 || (speeds[i][3]/speeds[i][1])>1)?e.childNodes[1].innerHTML:formatBytes(speeds[i][4]); //downloaded
        e.childNodes[4].innerHTML = speeds[i][5]>1024?formatBytes(speeds[i][5]):'';
        e.childNodes[6].innerHTML = formatBytes(speeds[i][6]);
        e.childNodes[7].innerHTML = speeds[i][7]>1024?formatBytes(speeds[i][7]):'';
        e.childNodes[8].innerHTML = speeds[i][8]/1000;
    }
});