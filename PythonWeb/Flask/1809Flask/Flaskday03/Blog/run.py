from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route("/list.html")
def index1():
    return render_template("list.html")


@app.route("/release")
@app.route("/release.html")
def index2():
    return render_template("release.html")


@app.route("/info")
@app.route("/info/<int:id_name>")
@app.route("/info.html")
@app.route("/info.html/<int:id_name>")
def index3(id_name=None):
    return render_template("info.html", id_name=id_name)


# 访问路径 /login
@app.route('/login')
@app.route('/login.html')
def login():
    return render_template('backup/login.html')


# 访问路径 /register
@app.route('/register')
@app.route('/register.html')
def register():
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)
