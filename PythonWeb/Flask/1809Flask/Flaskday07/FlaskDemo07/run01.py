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


# 创建实体类
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(30))
    uage = db.Column(db.Integer)
    uemail = db.Column(db.String(200))
    # 增加一个属性-isActive,默认值为True
    isActive = db.Column(db.Boolean, default=True)
    wife = db.relationship('Wife', backref='user', uselist=False)

    def __repr__(self):
        return "<User:%r>" % self.uname


# 创建Student实体类
class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(30))
    sage = db.Column(db.SmallInteger)
    isActive = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return "<User:%r>" % self.uname


# 创建Teacher实体类
class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(30), nullable=True)
    tage = db.Column(db.BigInteger, nullable=False)
    # 增加对Course(一)类的引用
    course_id = db.Column(
        db.Integer,
        db.ForeignKey('course.id')
    )


# 创建Course实体类
class Course(db.Model):
    """insert into course(cname) values("Python基础"), ("Python高级"), ("数据库基础"), ("Web基础"), ("服务器端开发");"""
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30), nullable=False)

    # 增加关联属性和反向引用关系
    # 关联属性:在course对象中通过哪个属性能够得到对应的所有的teacher对象
    # 反向引用:在teacher对象中通过哪个属性能够得到它对应的course
    teachers = db.relationship(
        'Teacher',
        backref="course",
        lazy="dynamic"
    )

    def __repr__(self):
        return "<Course:%r>" % self.cname


class Wife(db.Model):
    __tablename__ = 'wife'
    id = db.Column(db.Integer, primary_key=True)
    wname = db.Column(db.String(30))
    wage = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)

    def __repr__(self):
        return '<Wife:%r>' % self.wname


db.create_all()


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


@app.route('/06-add')
def add_to():
    users = User()
    users.uname = 'wang3'
    users.uage = 19
    users.uemail = 'wang114@163.com'
    db.session.add(users)
    return "添加成功"


@app.route('/07-delete/<int:uid>', methods=['GET', "POST"])
def delete_views(uid):
    """更新数据"""
    user = db.session.query(User).filter_by(id=uid).first()
    db.session.delete(user)
    return redirect('/table')


@app.route('/08-addteacher')
def addteacher_views():
    """
        每个teacher对象都有一个属性course_id（手动添加）
        每个teacher对象都有一个属性course（反向引用）
    """
    # 方式一：通过反向引用关系属性增加数据
    # 1。1获取ID为1的课程（course）对象
    # course = Course.query.filter_by(id=1).first()
    # # 创建teacher对象并制定数据
    # teacher = Teacher()
    # teacher.tname = "魏老师"
    # teacher.tage = 42
    # # 为teacher对象指定关联的course对象
    # teacher.course = course
    # # 将teacher传回数据库
    # db.session.add(teacher)

    # 方式二：通过外间类增加数据
    teacher = Teacher()
    teacher.tname = "王老师"
    teacher.tage = 31
    # 通过外间列添加数据
    teacher.course_id = 1
    db.session.add(teacher)
    return "教师添加成功"


@app.route("/09-regteacher", methods=["GET", "POST"])
def regteacher():
    if request.method == "GET":
        courses = Course().query.all()
        return render_template('09-rgeteacher.html', courses=courses)
    else:
        teacher = Teacher()
        teacher.tname = request.form['tname']
        teacher.tage = request.form['tage']
        teacher.course_id = request.form['course_id']
        db.session.add(teacher)
        return "注册成功"


# 通过course获取teachers
@app.route('/10-getteacher')
def getteacher_views():
    """通过course获取teachers"""
    # 1.获取id为1的的course信息
    course = Course.query.filter_by(id=1).first()
    # print(course.teachers)
    # print(type(course.teachers))
    teacher_list = course.teachers.all()
    for te in teacher_list:
        print(te.tname)
        print(te.tage)
    return '获取数据成功'


# 通过teacher获取course
@app.route('/10-getcourse')
def getcourse_views():
    """通过course获取teachers"""
    # 1.获取id为1的的course信息
    teacher = Teacher.query.filter_by(id=1).all()
    for co in teacher:
        print(co.course.cname)
    return '获取数据成功'


@app.route('/11-showteacher')
def showteacher():
    courses = Course.query.all()
    if "id" not in request.args or request.args['id'] == '0':
        teachers = Teacher.query.all()
    else:
        cid = request.args['id']
        print(cid)
        course = Course.query.filter_by(id=cid).first()
        teachers = course.teachers.all()
    return render_template('11-showteacher.html', params=locals())
    # return "get"


@app.route('/12-addwife')
def addwife():
    # # 通过外建属性user_id关联user与wife
    # wife = Wife()
    # wife.wname = "赵旭WC"
    # wife.wage = 38
    # wife.user_id = 2
    # db.session.add(wife)

    # 通过反向引用关系属性关联user与wife
    user = User.query.filter_by(id=3).first()
    wife = Wife()
    wife.wname = "SB赵旭"
    wife.wage = 250
    wife.user = user
    db.session.add(wife)
    return "增加数据成功"


@app.route('/12.5-regwife', methods=["GET", 'POST'])
def regwife():
    teachers = Teacher.query.all()
    if request.method == "GET":
        return render_template('12', teachers=teachers)
    else:
        wife = Wife()
        tid = request.form['id']
        teacher = Teacher.query.filter_by(id=tid).first()
        wife.wname = request.form['wname']
        wife.wage = request.form['wage']
        wife.teacher = teacher
        db.session.add(wife)
        return '添加成功'


@app.route('/13-queryuser')
def queryuser():
    if 'uname' in request.args:
        # 获取参数
        uname = request.args['uname']
        # 按照参数构建条件并查询数据
        user = User.query.filter(User.uname.like('%' + uname + '%')).all()
    else:
        user = User.query.all()
    return render_template('13-queryuser.html', params=locals())


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
        return render_template('adduser.html', users=users)
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
