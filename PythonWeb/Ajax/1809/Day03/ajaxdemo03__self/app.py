import json

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/flask05'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 自动实现提交
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['DEBUG'] = True
db = SQLAlchemy(app)

# 创建Manager对象并执行要管理哪个应用
manager = Manager(app)
# 创建Migrate的对象，并指定要关联的app和db
migrate = Migrate(app, db)
# 为Manager增加，允许数据表迁移的命令
manager.add_command('db', MigrateCommand)


class User1(db.Model):
    __tablename__ = 'user1'
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(30))
    uage = db.Column(db.Integer)
    upwd = db.Column(db.String(200))
    nickname = db.Column(db.String(50))

    def to_dict(self):
        dic = {
            'id': self.id,
            'uname': self.uname,
            'uage': self.uage,
            'upwd': self.upwd,
            'nickname': self.nickname
        }
        return dic


db.create_all()




@app.route('/')
@app.route('/index')
def hello_world():
    # user = User1()
    # user.uname = "wang2"
    # user.uage = "20"
    # user.upwd = "111111"
    # user.nickname = "wang2"
    # db.session.add(user)
    return 'Hello World!'


@app.route('/01-load', methods=['GET', "POST"])
def hello_load():
    if request.method == "GET":
        name = request.args['name']
        age = request.args['age']
        return '姓名：%s, 年龄： %s' % (name, age)
    else:
        name = request.form['name']
        age = request.form['age']
        return '姓名：%s, 年龄： %s' % (name, age)


@app.route('/03-server')
def hello_get1():
    user = User1.query.all()
    list = []
    for u in user:
        list.append(u.to_dict())
    return json.dumps(list)


@app.route('/04-server')
def hello_get2():
    uname = request.args['uname']
    uage = request.args['uage']
    return '使用GET方式请求的数据为:\r\n uname %s, uage %s' % (uname, uage)


@app.route('/05-find')
def find():
    list = []
    key = request.args['key']
    users = User1.query.filter(User1.uname.like('%' + key + '%')).all()
    for u in users:
        list.append(u.to_dict())
    print(list)
    return json.dumps(list)



if __name__ == '__main__':
    manager.run()
