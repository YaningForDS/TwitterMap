from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import json
import redis


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/GoogleMap')
def GoogleMap():
    return render_template("yuxx0431calendar.html")



@socketio.on('connected')
def keyword(message):
    print ('Client connected')



@socketio.on('disconnect')
def test_disconnect():
    print ('Client disconnected')



if __name__ == "__main__":
    app.run()


