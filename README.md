# pseedbox

## Description

pseedbox is a web user interface for [rTorrent](https://github.com/rakshasa/rtorrent) client. It uses websockets for an interactive display.

## Roadmap

- Communicate with rTorrent + UNIX socket support
- User interface
- Multiple user account with expiration
- Add/remove a torrent
- Batch tracker upgrade
- Scrappe files to build a media library (without playback)
- Virtual filesystem (for FTP/sFTP)
- Monitor RSS/atom feed

## Installation

### rTorrent
Edit your ``~/.rtorrent.rc``  config file, add the following line if not exists:

> ``scgi_port = 127.0.0.1:5000``

### pseedbox

### nginx

