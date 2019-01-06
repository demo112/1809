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
    uemail = db.Column(db.String(50), nullable=False)
    nickname = db.Column(db.String(50), nullable=False)
    uphone = db.Column(db.String(11))
    upwd = db.Column(db.String(200), nullable=False)

    def __init__(self, uemail, nickname, uphone, upwd):
        self.uemail = uemail
        self.nickname = nickname
        self.uphone = uphone
        self.upwd = upwd


@app.route('/')
@app.route('/index')
@app.route('/guoyuan')
def index_views():
    # todo 完善判断逻辑：cookies和session
    # 判断session中是否有uname
    # if 'uname' in session:
    #     uname = session.get('uname')
    #     user = User.query.filter_by(uname=uname).first()
    return render_template('index.html', params=locals())


@app.route('/signin', methods=['GET', 'POST'])
def register_views():
    if request.method == 'GET':
        return render_template('signin.html')
    else:
        uemail = request.form['uemail']
        nickname = request.form['nickname']
        uphone = request.form['uphone']
        upwd1 = request.form['upwd1']
        upwd2 = request.form['upwd2']
        if upwd1 == upwd2:
            upwd = generate_password_hash(upwd1)
            user = User(uemail, nickname, uphone, upwd)
            # 使用generate_password_hash()对upwd进行加密,并接收加密后的结果
            db.session.add(user)
            # 将数据保存进session即可
            session['nickname'] = user.nickname
            return redirect('/')
        else:
            return render_template('signin.html', errMsg='用户密码不一致')


@app.route('/check')
def check():
    name = request.args['uemail']
    tag = request.args['tag']
    print(name, tag, 3)
    if tag == 'uemail':
        user = User.query.filter_by(uemail=name).first()
        if user:
            msg = '已被使用'
        else:
            msg = '允许使用'
        return msg
    elif tag == 'nickname':
        user1 = User.query.filter_by(nickname=name).first()
        if user1:
            msg = '已被使用'
        else:
            msg = '允许使用'
        return msg
    elif tag == 'uphone':
        user2 = User.query.filter_by(uphone=name).first()
        if user2:
            msg = '已被使用'
        else:
            msg = '允许使用'
        return msg


@app.route('/signup', methods=['GET', "POST"])
def login_views():
    if request.method == "GET":
        url = request.headers.get('Referer', '/')
        session['url'] = url
        if 'uphone' in session:
            # 判断session是有存在
            return redirect(url)
        # 继续判断cookie有没有保存密码
        if 'uphone' in request.cookies:
            user = User.query.filter_by(uname=request.cookies['uphone']).first()
            if user and check_password_hash(user.upwd, request.cookies['upwd']):
                return render_template('index.html')
        return render_template('signup.html')
    else:
        uphone = request.form['uphone']
        upwd = request.form['upwd']
        print(uphone, upwd)
        # 验证用户名即密码是否正确
        user = User.query.filter_by(uphone=uphone).first()
        if user and check_password_hash(user.upwd, upwd):
            print('登陆成功')
            # 将uname的值放入session
            session['uphone'] = uphone
            # 判断是否要存cookie
            url = session.get('url', '/')
            resp = redirect(url)
            if 'remember' in request.form:
                resp.set_cookie('uphone', uphone, 60 * 60 * 24 * 365 * 20)
                """此处密码是明文"""
                resp.set_cookie('upwd', upwd, 60 * 60 * 24 * 365 * 20)
            return resp
        else:
            # 登陆失败
            return render_template('signup.html', errMSG="用户名或密码不正确1")


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


if __name__ == "__main__":
    manager.run()
