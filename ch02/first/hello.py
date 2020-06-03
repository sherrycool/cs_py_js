#%%
#tb
'''
from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return("My first Python Web")
#生成app实例，传递 __name__参数，__name__ 就是当前模块名字。
 # terminal: export FLASK_APP=application.py
  # export FLASK_ENV=development
# flask run
if __name__=='__main__':
    app.run(host='0.0.0.0',debug = True)
    '''
#%%
from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def index():
    return(render_template('./template/index.html'))

if __name__=='__main__':
    app.run(host='0.0.0.0',debug = True)

# %%
'''
from flask import request
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

'''
