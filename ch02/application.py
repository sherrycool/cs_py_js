from flask import Flask
 
app = Flask(__name__)  
#生成app实例，传递 __name__参数，__name__ 就是当前模块名字。
 # terminal: export FLASK_APP=application.py
  # export FLASK_ENV=development
# flask run

@app.route("/")
def index():
    return "hello world"
 
 

