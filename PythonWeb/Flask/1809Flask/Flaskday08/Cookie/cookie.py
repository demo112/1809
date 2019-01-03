from flask import make_response, request, render_template
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/login_guoyuan'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 自动实现提交
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'bgfasdfsdfsvbewioranhgviowegobirvwnilbuesrh'

db = SQLAlchemy(app)

# 创建Manager对象并执行要管理哪个应用
manager = Manager(app)
# 创建Migrate的对象，并指定要关联的app和db
migrate = Migrate(app, db)
# 为Manager增加，允许数据表迁移的命令
manager.add_command('db', MigrateCommand)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(100), unique=True)
    upsw = db.Column(db.String(100), unique=True)


db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/adduser')
def adduser():
    user = User()
    user.uname = 'qu'
    user.upsw = '222222'
    db.session.add(user)
    flag = '成功注册'
    return render_template('index.html', flag=flag)


@app.route('/01-addcookies')
def addcookies():
    reps = make_response("添加成功")
    reps.set_cookie("uname", "zhaoxuSB", 60 * 60 * 24 * 365 * 100)
    return reps


@app.route('/02-getcookies')
def getcookies():
    req = request.cookies
    print(req['uname'])
    return "got it"


@app.route('/02-deletecookies')
def deletecookies():
    req = make_response("delete it")
    req.delete_cookie('uname')
    return req


@app.route('/03-register', methods=['GET', 'POST'])
def regsiter():
    if request.method == "GET":
        if 'uname' in session and 'upsw' in session:
            print('session验证成功')
            req = make_response(render_template('index.html'))
            return req

        if 'uname' in request.cookies and 'upsw' in request.cookies:
            uname = request.cookies["uname"]
            upsw = request.cookies["upsw"]
            if uname == upsw == 'admin':
                session['uname'] = request.cookies['uname']
                session['upsw'] = request.cookies['upsw']
                print('cookie验证成功')
                return render_template('index.html')
            else:
                return render_template('03-regster.html', errMsq='用户名或密码不正确1')
        return render_template('03-regster.html')
    else:
        if request.form['uname'] and request.form['upsw']:
            if request.form['uname'] == "admin" and request.form['upsw'] == 'admin':
                # 给session村数据
                req = make_response(render_template('index.html'))

                # 创建静态页面对象，判断是否记住密码
                if 'remember' in request.form:
                    max_age = 60 * 60 * 24 * 365 * 100
                    req.set_cookie("uname", request.form['uname'], max_age)
                    req.set_cookie("upsw", request.form['upsw'], max_age)
                    print(request.form['remember'])
                return req
            else:
                return render_template('03-regster.html', errMsq='用户名或密码不正确2')
        else:
            return render_template('03-regster.html', errMsq='输入为空')



@app.route('/01-addsession')
def addsession():
    session['uname'] = "admin"
    session['upsw'] = 'admin'
    return "向session中添加数据成功"


@app.route('/02-getsession')
def getsession():
    if 'uname' in session and "upsw" in session:
        uname = session['uname']
        upsw = session['upsw']
        print(uname, upsw)
        return "获取session数据成功"
    else:
        return "session中没有数据"


if __name__ == '__main__':
    manager.run()
