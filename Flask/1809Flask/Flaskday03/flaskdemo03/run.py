from flask import Flask, render_template

app = Flask(__name__)


@app.route('/01-url')
def url_for():
    return render_template("01-url.html")


if __name__ == "__main__":
    app.run(debug=True)
