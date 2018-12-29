from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy import or_

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
    user.uname = "rapwang"
    user.uage = 15
    user.uemail = 'wang163@163.com'
    # 通过db.commit保存实体对象
    db.session.add(user)
    return 'Commit Success!!!'


@app.route('/02-query')
def query_views():
    """获取查询对象"""
    query = db.session.query(User)

    # query_id = db.session.query(User.id, User.uname)
    # querys = db.session.query(User, Student, Teacher)
    # print(query, '\r\n', query_id, '\r\n', querys)
    # print(type(query))

    """查询执行函数"""
    al = query.all()
    print(al)
    # 示例：查询所有的信息
    for i in al:
        print("id:%d, uname:%s, uage:%d, uemail:%s" % (i.id, i.uname, i.uage, i.uemail))

    # 练习：查询所有数据的id和name
    users = db.session.query(User.id, User.uname)
    for i in users:
        print("id:%d, uname:%s" % (i.id, i.uname))

    fist = query.first()
    print(fist)

    fist_or_404 = query.first_or_404()
    print(fist_or_404)

    """获取数据的数量"""
    count = query.count()
    print(count)

    """查询对象选择器"""

    """filter"""
    # young = db.session.query(User).filter(or_(User.uage >= 10, User.id > 2)).all()
    # young2 = db.session.query(User).filter(User.id == 2).first()
    # young3 = db.session.query(User).filter_by(id=3).first()
    # # 性能优化
    # young23 = db.session.query(User).filter(User.uage >= 18, User.uage <= 18).all()
    # young4 = db.session.query(User).filter(User.uemail.like('%w%')).all()
    # young5 = db.session.query(User).filter(User.uage.in_([16, 18, 19])).all()
    # young6 = db.session.query(User).filter(User.uage.between(16, 19)).all()
    # print(
    #     young, '\n',
    #     young2, '\n',
    #     young3, '\n',
    #     young23, '\n',
    #     young4, '\n',
    #     young5, '\n',
    #     young6, '\n',
    #     '\n'
    # )
    """其他"""
    young7 = db.session.query(User).limit(2).offset(4).all()
    young8 = db.session.query(User).order_by("id desc").first().uage
    young9 = db.session.query(User).order_by("uage desc, id asc").first().uage
    print(
        young7, '\n',
        young8, '\n',
        young9, '\n',
        '\n'
    )
    return "<script>" \
           "alert('查询成功')" \
           "</script>"


@app.route('/03-select')
def select_views():
    users = db.session.query(User).all()
    return render_template('form.html', users=users)


if __name__ == '__main__':
    manager.run()
