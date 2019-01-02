from fileinput import fileno

from flask import Flask
# from numpy.doc import  / f

app = Flask(__name__)


@app.route("/")
def index():
    f = open('网页/index.html', "r")
    date = f.read()
    f.close()
    print(date)
    return date


if __name__ == "__main__":
    app.run(debug=True)
