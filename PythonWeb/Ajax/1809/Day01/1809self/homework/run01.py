from flask import Flask, render_template, render_template_string, request
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
"""重复用户名提醒，强行提交无法注册"""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@127.0.0.1:3306/ajax"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'you guess'
db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(100))
    upwd = db.Column(db.String(100))
    nickname = db.Column(db.String(100))


# def check_reapet():

@app.route('/01-checkuname')
def checkuname():
    uname = request.args['uname']
    user = User.query.filter_by(uname=uname).first()
    if user:
        return "用户存在"
    else:
        return "可以使用"


@app.route('/02-register', methods=['POST'])
def register_post():
    uname = request.form['uname']
    upwd = generate_password_hash(request.form['upwd'])
    nickname = request.form['nickname']
    user = User.query.filter_by(uname=uname).first()
    if user:
        return "用户已存在"
    else:
        user =User()
        user.uname = uname
        user.upwd = upwd
        user.nickname = nickname
        try:
            db.session.add(user)
            db.session.commit()
            print(request.form)
            return "接收到请求"
        except Exception as e:
            print(e)
            return "注册失败"


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
