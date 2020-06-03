import datetime
from flask import Flask, render_template

app = Flask(__name__)

# condition example
@app.route("/")
def index():
    now = datetime.datetime.now()
    is_new_year = now.month == 1 and now.day == 1
    return render_template("index.html", is_new_year=is_new_year)

# loop example
@app.route("/loop")
def loopE():
    names = ['Alice', 'Bob', 'Charlie']
    return render_template('loop.html', names=names)


@app.route("/more")
def more():
    return render_template('more.html')


if __name__ == "__main__":
    app.run(debug=True)
