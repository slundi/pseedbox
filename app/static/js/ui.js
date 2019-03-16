/* Dialogs */
function add_torrent_dialog(e) {
    alert("Add a torrent");
}
function manage_premium_account_dialog() {
    
}
function edit_torrent() {
    
}
function show_modal(id)  {document.getElementById(id).style.display='block';}
function close_modal(id) {document.getElementById(id).style.display='none';}
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
/* Events */
document.addEventListener('click', function(event) {
    //close opened modal
    var modals = document.getElementsByClassName("modal");
    Array.prototype.forEach.call(modals, function(e){if(e.style.display!='none' && !e.firstChild.contains(event.target)) e.style.display='none';});
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
/* Table */
function resizableThead(id){
    
}
resizableThead('torrents');