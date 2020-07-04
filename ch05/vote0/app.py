import requests

import os
from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

# 跨域时使用下面的
#socketio = SocketIO(app,cors_allowed_origins="*") 

@app.route("/")
def index():
	return render_template("index.html")

# js中emit的对象，当套接字检测到此事件时，将连接到下面这个特定功能
@socketio.on("submit vote") 
def vote(data):
	selection = data['selection']
	emit("announce vote", {"selection":selection}, broadcast=True)

'''
def main():
	socketio.run(app, debug=True)

if __name__ == "__main__":
	main()

这里例子里，不能这么执行 只能在terminal里；
cd eg2
flask run

不好理解的地方在于前端和后端的交互
前端行为是啥，导致后端干了啥
后端干了啥，又反应在前端上
	'''