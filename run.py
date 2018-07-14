from app import app, socketio
import os
import config

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    socketio.run(app, host = HOST, port = config.SERVER_PORT, debug=True)
