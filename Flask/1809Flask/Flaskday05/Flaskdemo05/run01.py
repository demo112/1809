from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

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


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(30))
    uage = db.Column(db.Integer)
    uemail = db.Column(db.String(200))


class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(30))
    sage = db.Column(db.Integer)
    isActive = db.Column(db.Boolean, default=True)


class Teacher(db.Model):
    __tablename__ = "teacher"
    id = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(30))
    tage = db.Column(db.Integer)


class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(50))


@app.route('/')
def index():
    return "This is my first page"


@app.route('/01-adduser', methods=["GET", "POST"])
def adduser_views():
    # 创建user实体
    user = User()
    user.uname = "wang"
    user.uage = 18
    user.uemail = 'wang163@163.com'
    # 通过db.commit保存实体对象
    db.session.add(user)
    return 'Commit Success!!!'


@app.route('/01-query')
def query_views():
    query = db.session.query(User)
    query_id = db.session.query(User.id, User.uname)
    querys = db.session.query(User, Student, Teacher)
    print(query, '\r\n', query_id, '\r\n', querys)
    print(type(query))
    return "<script>" \
           "alert('查询成功')" \
           "</script>"


if __name__ == '__main__':
    manager.run()
