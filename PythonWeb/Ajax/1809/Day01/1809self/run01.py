from flask import Flask, request

app = Flask(__name__)


@app.route('/02-server')
def server01_views():
    return "This is my first response by Ajax"


@app.route('/03-server')
def server03_views():
    uname = request.args['uname']
    return "欢迎" + uname


if __name__ == '__main__':
    app.run(debug=True)
