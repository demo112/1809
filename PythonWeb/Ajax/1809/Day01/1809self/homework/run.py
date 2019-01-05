from flask import Flask, render_template, render_template_string, request
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy


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


@app.route('/adduser')
def adduser():
    user = User()
    user.uname = 'cooper'
    user.upwd = '111111'
    user.nickname = 'coco'
    db.session.add(user)
    return ''


@app.route('/')
@app.route('/signin', methods=['GET',"POST"])
def signin():
    if request.method == "GET":
        return render_template('signin.html')
    else:
        uname = request.form['uname']
        upwd = request.form['upwd']
        user = User.query.filter_by(uname=uname).first()
        if user and upwd == user.upwd:
             return render_template('index.html')


@app.route('/check')
def check():
    print(11)
    uname = request.args['uname']
    print(uname)
    user = User.query.filter_by(uname=uname).first()
    if user:
        return '用户已存在'
    else:
        return '允许使用'


if __name__ == '__main__':
    manager.run()
