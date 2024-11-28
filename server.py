# server.py

from flask import Flask, render_template
from flask_socketio import SocketIO, send

"""
    Inisiasi socket
"""
app = Flask(__name__)
socketio = SocketIO(app)

"""
    Route halaman utama
"""
@app.route('/')
def index():
    return render_template('index.html')

"""
    Socket message handler
"""
@socketio.on('message')
def handle_message(msg):
    print('Received message: ' + msg)
    send(msg, broadcast=True)  # Kirim pesan ke semua client

"""
    Jalankan server
"""
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
