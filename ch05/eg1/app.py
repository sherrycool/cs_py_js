import requests

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/convert", methods=['POST'])
def convert():
    # query for currency exchange rate
    tocoin = request.form.get('currency')
	
    fromcoin = 'CNY'
    key = '795abf092e9fde6d3da9bd649bcbadc9'
    money = 1
    res = requests.get("http://api.tianapi.com/txapi/fxrate/index",
                       params={'key': key, 'tocoin': tocoin,
                               "fromcoin": fromcoin, 'money': money})
    # make sure request succeeded
    if res.status_code != 200:
        # raise Exception("ERROR: API request unsuccessful.")
        return jsonify({"success": False})

    # make sure currency is in response rate = data['newslist'][0]['money']
    # {'code': 200, 'msg': 'success', 'newslist': [{'money': '0.0652'}]}
    data = res.json()
    '''
    if data['msg'] == '数据返回为空':
        return jsonify({"success", False})
    else:
        rate = data['newslist'][0]['money']
        return jsonify({"success": True, 'rate':data['newslist'][0]['money']})
    '''
    try:
        rate = data['newslist'][0]['money']
        return jsonify({"success": True, 'rate':data['newslist'][0]['money']})
    except:
        return jsonify({"success": False})


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()