from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return "这是blog的首页"


@app.route("/list")
def index1():
    return "这是blog的列表页"


@app.route("/release")
def index2():
    return "这是blog的发表页"


@app.route("/info/<int:id_name>")
def index3(id_name):
    return "查看id为%s的blog信息" % id_name


if __name__ == "__main__":
    app.run(debug=True)
