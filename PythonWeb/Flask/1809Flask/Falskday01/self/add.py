from flask import Flask
app = Flask(__name__)


@app.route('/calc/<int:a>/<int:b>')
def add(a,b):
    c = str(a + b)
    return c


if __name__ == "__main__":
    app.run(debug=True)