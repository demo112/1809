from flask import Flask, request, render_template, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@127.0.0.1:3306/login_guoyuan"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'you guess'
db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(30))
    upwd = db.Column(db.String(200))
    nickname = db.Column(db.String(50))

    def __init__(self, uname, upwd, nickname):
        self.uname = uname
        self.upwd = upwd
        self.nickname = nickname


@app.route('/01-register', methods=['GET', 'POST'])
def register_views():
    if request.method == 'GET':
        return render_template('01-register.html')
    else:
        uname = request.form['uname']
        upwd = request.form['upwd']
        nickname = request.form['nickname']
        # 使用generate_password_hash()对upwd进行加密,并接收加密后的结果
        upwd = generate_password_hash(upwd)
        user = User(uname, upwd, nickname)
        db.session.add(user)
        # 将数据保存进session即可
        session['uname'] = uname
        return redirect('/')


@app.route('/')
def index_views():
    # 判断session中是否有uname
    if 'uname' in session:
        uname = session.get('uname')
        user = User.query.filter_by(uname=uname).first()
    return render_template('index.html', params=locals())


@app.route('/logout')
def logout_views():
    url = request.headers.get('Referer', '/')
    resp = redirect(url)
    # 判断session中是否有uname,如果有的话则清空
    if 'uname' in session:
        del session['uname']
    # 判断cookie中是否有uname,如果有则清空
    if 'uname' in request.cookies:
        resp.delete_cookie('uname')
    # 返回到"从哪来回哪去,不知道从哪来回首页"
    return resp


@app.route('/login', methods=['GET', "POST"])
def login_views():
    if request.method == "GET":
        url = request.headers.get('Referer', '/')
        session['url'] = url
        if 'uname' in session:
            # 判断session是有存在
            return redirect(url)
        # 继续判断cookie有没有保存密码
        if 'uname' in request.cookies:
            user = User.query.filter_by(uname=request.cookies['uname']).first()
            if user and check_password_hash(user.upwd, request.cookies['upwd']):
                return render_template('index.html')

        return render_template('login.html')
    else:
        uname = request.form['uname']
        upwd = request.form['upwd']
        # 验证用户名即密码是否正确
        user = User.query.filter_by(uname=uname).first()
        if user and check_password_hash(user.upwd, upwd):
            # 登陆成功
            # 将uname的值放入session
            session['uname'] = uname
            # 判断是否要存cookie
            url = session.get('url', '/')
            resp = redirect(url)
            if 'isSave' in request.form:
                resp.set_cookie('uname', uname, 60 * 60 * 24 * 365 *20)
                """此处密码是明文"""
                resp.set_cookie('upwd', upwd, 60 * 60 * 24 * 365 *20)
            return resp
        else:
            # 登陆失败
            return render_template('login.html',errMSG="用户名或密码不正确1")


if __name__ == "__main__":
    manager.run()