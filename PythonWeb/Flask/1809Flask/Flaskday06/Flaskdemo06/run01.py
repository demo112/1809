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


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(30))
    uage = db.Column(db.Integer)
    uemail = db.Column(db.String(200))
    isActive = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return "<User:%r>" % self.uname


class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(30))
    sage = db.Column(db.Integer)
    isActive = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return "<User:%r>" % self.uname


class Teacher(db.Model):
    __tablename__ = "teacher"
    id = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(30))
    tage = db.Column(db.Integer)

    def __repr__(self):
        return "<User:%r>" % self.uname


class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(50))

    def __repr__(self):
        return "<User:%r>" % self.uname


@app.route('/')
def index():
    return "This is my first page"


@app.route('/01-adduser', methods=["GET", "POST"])
def adduser_views():
    # 创建user实体
    user = User()
    user.uname = "glodrapwang"
    user.uage = 1008
    user.uemail = 'wang163@163.com'
    # user.isActive = False
    # 通过db.commit保存实体对象
    db.session.add(user)
    return 'Commit Success!!!'


@app.route('/02-query')
def query_views():
    """获取查询对象"""
    query = db.session.query(User)
    query_id = db.session.query(User.id, User.uname)
    querys = db.session.query(User, Student, Teacher)
    print(query, '\r\n', query_id, '\r\n', querys)
    print(type(query))
    return "<script>" \
           "alert('查询成功')" \
           "</script>"


@app.route('/03-select')
def select_views():
    users = db.session.query(User).all()
    return render_template('form.html', users=users)


@app.route('/05func')
def func_views():
    """聚合函数的使用"""
    """查询user表中的所有人的平均年龄"""
    avg_age1 = db.session.query(func.avg(User.uage)).first()
    """按照age进行分组求每组中平均年龄，和总和"""
    avg_age = db.session.query(User.uage, func.avg(User.uage), func.sum(User.uage)).group_by('uage').all()
    print(avg_age)
    print(avg_age1)
    print(avg_age[0])
    return "chenggong"


@app.route('/add')
def add_to():
    users = User()
    users.uname = 'wang3'
    users.uage = 19
    users.uemail = 'wang114@163.com'
    db.session.add(users)
    return "添加成功"


@app.route('/check')
def check_views():
    print(db.session.query(User).all())
    return "checked Success"


@app.route('/table', methods=['GET', "POST"])
def table_views():
    users = db.session.query(User).all()
    return render_template('table.html', users=users)


@app.route('/adduser', methods=['GET', "POST"])
def add_views():
    if request.method == "GET":
        users = db.session.query(User).all()
        return render_template('adduser.html',users=users)
    else:
        user = User()
        user.uname = request.form.get('uname')
        user.uage = request.form.get('uage')
        user.uemail = request.form.get('uemail')
        db.session.add(user)
        return redirect('/table')


@app.route('/update', methods=['GET', "POST"])
def change_views():
    """更新数据"""
    if request.method == "GET":
        users = db.session.query(User).all()
        indexs = request.args.get('id')
        user = db.session.query(User).filter_by(id=indexs).first()
        print(user, indexs)
        return render_template('table_change.html', user=user, users=users)
    else:
        indexs = request.form.get('id')
        user = db.session.query(User).filter_by(id=indexs).first()
        print(indexs)
        print(user)
        user.uname = request.form.get('uname')
        user.uage = request.form.get('uage')
        user.uemail = request.form.get('uemail')
        db.session.add(user)
        # return render_template('table_change.html', users=users)
        # 将请求重新定向到table上
        return redirect('/table')


@app.route('/delete/<int:id>', methods=['GET', "POST"])
def delete_views(id):
    """更新数据"""
    user = db.session.query(User).filter_by(id=id).first()
    db.session.delete(user)
    return redirect('/table')


@app.route('/count')
def count_views():
    """有条件聚合函数查询"""
    count = db.session.query(User.isActive, func.count(User.isActive)).group_by(User.isActive).all()
    print(count)
    return "chaxunchenggong"


@app.route('/count2')
def count_views2():
    index2 = db.session.\
        query(User.isActive, func.count(User.isActive)).\
        group_by(User.isActive).\
        having(func.count(User.isActive) > 2).\
        all()

    for i in range(len(index2)):
        print(index2[i])
    return "chenggong"


if __name__ == '__main__':
    manager.run()
