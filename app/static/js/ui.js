/* Dialogs */
function add_torrent_dialog(e) {
    show_modal('add_torrent');
}
function manage_premium_account_dialog() {
    
}
function edit_torrent() {
    
}
function show_modal(id)  {document.getElementById(id).style.display='block';}
function close_modal(id) {document.getElementById(id).style.display='none';}
function close_opened_modals() {
    //close opened modal
    var modals = document.getElementsByClassName("modal");
    Array.prototype.forEach.call(modals, function(e){if(e.style.display!='none' && !e.firstChild.contains(event.target)) e.style.display='none';});
}
/* Right-click menu */
function set_global_download_speed() {

}
function set_global_upload_speed() {

}

/* Filter functions */
function clear_filters(searchbox=true) {
    console.log('Clear filters')
    if(searchbox) document.getElementById('search').value='';
    var filters = document.getElementsByClassName("filter");
    Array.prototype.forEach.call(filters, function(e){e.setAttribute('class', 'filter');});
}
function filter_status(s) {

}
function filter_label(l) {

}
function filter_tracker(s) {

}
function filter_user(u) {

}
function search(txt) {
    
}
/* Table */
function resizableThead(id){
    
}
resizableThead('torrents');
/* Misc */
function bytesToSize(bytes) {
    var sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
    if (bytes == 0) return '0 Byte';
    var i = parseInt(Math.floor(Math.log(bytes) / Math.log(1024)));
    return Math.round(bytes / Math.pow(1024, i), 2) + ' ' + sizes[i];
 }
 function change_language(code) {
    //TODO: load i18n/lang.code.js
    //process content and title attributes
    ['span', 'label', 'small', 'h1', 'h2', 'h3', 'h4', 'h5', 'a', 'li', 'ht'].forEach(function(tag){
        if(tag.hasAttribute('data-i18n')) {
            l=document.getElementsByTagName(tag);
            l.forEach(function(e){
                //TODO: replace keys e.innerHTML=
            });
        }
    });
    //buttons ?
    //process placeholder attributes
    document.getElementsByTagName("input");
    document.getElementsByTagName("textarea");
 }
/* Events */
document.addEventListener('click', function(event) {
    close_opened_modals();
    //filters
    var filters = document.getElementsByClassName("filter");
    Array.prototype.forEach.call(filters, function(e){
        if(e.contains(event.target)) {
            console.log('It\'s me... a filter')
            clear_filters();
            e.setAttribute('class', 'filter active');
        }
    });
});
document.addEventListener('dragover', function(e){e.preventDefault();});
document.addEventListener('', function(e){e.preventDefault();e.stopPropagation();});
document.getElementById('files').addEventListener('change', function(e) {
    var input=document.getElementById('files');
    var files=input.files;
    for(i=0; i<files.length;i++) {
        console.log(files[i].name);
        //TODO: list files[i].name (with files[i].size) below input
    }
});
function drop_torrents(e) {
    console.log('File(s) dropped');
    // Prevent default behavior (Prevent file from being opened)
    e.preventDefault();
    e.stopPropagation();
}
document.addEventListener('keydown', function(e) {
    //ignored keys
    if(e.target.tagName == 'INPUT' || e.target.tagName == 'SELECT' || e.target.tagName == 'TEXTAREA'
        || (e.keyCode >= 37 && e.keyCode <= 40) //arrow keys 37-40
        || e.keyCode == 33 || e.keyCode==34 //page up & down 33, 34
    ) return false;
    //commands
    if(e.keyCode == 112) show_modal('keyboard_shortcuts');
    if(e.ctrlKey && e.keyCode == 79) show_modal('add_torrent');
    if(e.ctrlKey && e.keyCode == 70) document.getElementById('search').focus();
    if(e.keyCode == 46 || e.keyCode == 8) delete_torrent();
    if(e.shiftKey && e.keyCode == 46) delete_torrent(false);
    if(e.keyCode == 27) close_opened_modals(); //escape key
    e.preventDefault();
}); 