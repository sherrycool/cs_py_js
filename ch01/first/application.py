from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!" 

@app.route("/david")
def david():
    return "Hello, David!" 


@app.route("/maria")
def maria():
    return "Hello, Maria!" 

if __name__=='__main__':
    app.run(host='0.0.0.0',debug = True)