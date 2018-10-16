import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    hb = now.month == 10 and now.day == 17
    return render_template("index.html", hb=hb)

if (__name__ == "__main__"):
	app.run(debug=True)
