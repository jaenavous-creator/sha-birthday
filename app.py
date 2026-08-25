from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/memories")
def memories():
    return render_template("memories.html")


@app.route("/message")
def message():
    return render_template("message.html")


@app.route("/letter")
def letter():
    return render_template("letter.html")


if __name__ == "__main__":
    app.run(debug=True)