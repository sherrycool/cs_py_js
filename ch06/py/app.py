from flask import Flask, render_template, request
import requests
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('currency.html')


@app.route('/rate', methods=['POST'])
def rate():
    tocoin = request.form.get('tocoin')
    fromcoin = 'CNY'
    key = '795abf092e9fde6d3da9bd649bcbadc9'
    money = 1
    res = requests.get("http://api.tianapi.com/txapi/fxrate/index",
                       params={'key': key, 'tocoin': tocoin,
                               "fromcoin": fromcoin, 'money': money})
    if res.status_code != 200:
        # raise Exception("ERROR: API request unsuccessful.")
        return render_template('error.html',
                               message="ERROR: API request unsuccessful.",
                               message2=None)

    data = res.json()
    try:
        rate = data['newslist'][0]['money']
    except KeyError:
        return render_template('error.html',
                               message="ERROR: ", message2=data)

    return render_template('currency.html', fromcoin=fromcoin, tocoin=tocoin,
                           rate=rate)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
