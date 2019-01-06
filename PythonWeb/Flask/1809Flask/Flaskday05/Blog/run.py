from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# import hashlib


# m = hashlib.sha256()
# m.update(b"Nobody inspects")
# m.update(b" the spammish repetition")
# m.digest()


# 为app指定配置
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True, index=True)
    email = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(200), nullable=True)
    password = db.Column(db.String(200), nullable=False)


db.create_all()


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
@app.route('/login', methods=["GET", "POST"])
@app.route('/login.html', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('backup/login.html')
    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        return '用户名：%s, 密码：%s' % (username, password)


# 访问路径 /register
@app.route('/register')
@app.route('/register.html')
def register():
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)
