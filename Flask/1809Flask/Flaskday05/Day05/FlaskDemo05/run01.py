from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy import or_, func

pymysql.install_as_MySQLdb()

app = Flask(__name__)
#指定数据库的配置
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:123456@localhost:3306/flask"
#指定当视图执行完毕后,自动提交数据库操作
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
#指定每次执行操作时打印原始的SQL语句
# app.config['SQLALCHEMY_ECHO']=True
#创建数据库的实例
db = SQLAlchemy(app)

#创建实体类
class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),nullable=False,unique=True)
    age = db.Column(db.Integer)
    email = db.Column(db.String(120),unique=True)

    def __init__(self,username,age,email):
        self.username = username
        self.age = age
        self.email = email

    def __repr__(self):
        return "<Users:%r>" % self.username

class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer,primary_key=True)
    sname = db.Column(db.String(30),nullable=False)
    sage = db.Column(db.Integer)

    def __init__(self,sname,sage):
        self.sname = sname
        self.sage = sage

    def __repr__(self):
        return "<Student:%r>" % self.sname

class Teacher(db.Model):
    __tablename__ = "teacher"
    id = db.Column(db.Integer,primary_key=True)
    tname = db.Column(db.String(30),nullable=False)
    tage = db.Column(db.Integer)
    tbirth = db.Column(db.Date)

    def __init__(self,tname,tage,tbirth):
        self.tname = tname
        self.tage = tage
        self.tbirth = tbirth

    def __repr__(self):
        return "<Teacher:%r>" % self.tname

class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer,primary_key=True)
    cname = db.Column(db.String(30),nullable=False)

    def __init__(self,cname):
        self.cname = cname

    def __repr__(self):
        return "<Course:%r>" % self.cname

db.create_all()


@app.route('/01-add')
def add_views():
    #创建Users对象,并插入到数据库中
    users = Users('王老师',35,'mrwang@163.com')
    db.session.add(users)
    db.session.commit()
    return "Add OK"

@app.route('/02-register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('02-register.html')
    else:
        #接收前端传递过来的数据
        uname = request.form.get('uname')
        uage = request.form.get('uage')
        uemail = request.form.get('uemail')
        #将数据构建成实体对象
        user = Users(uname,uage,uemail)
        #将数据保存回数据库
        db.session.add(user)
        # db.session.commit()
        return "Register Success"

@app.route('/03-query')
def query_views():
    # 测试 all() 函数
    # users = db.session.query(Users).all()
    # for u in users:
    #     print('姓名:%s,年龄:%d,邮箱:%s' % (u.username,u.age,u.email))

    # 测试 first() 函数
    # user = db.session.query(Users).first()
    # print(user)

    # 测试查询返回部分列
    # select username,age from users
    # query=db.session.query(Users.username,Users.age)
    # print(query)

    ###################
    # 测试 filter() 函数
    ##################
    # filter() - 查询 Users中年龄大于30的人的信息
    # users=db.session.query(Users).filter(Users.age>30).all()

    # filter() - 查询Users中id大于1并且年龄大于30的人的信息
    # users = db.session.query(Users).filter(Users.age>30,Users.id>1).all()

    #filter() - 查询Users中id为1或者年龄大于30的人的信息
    # users = db.session.query(Users).filter(or_(Users.id==1,Users.age > 30)).all()

    #filter() - 查询Users中id在[2,4]列表中的users的信息
    # users = db.session.query(Users).filter(Users.id.in_([2,4])).all()

    #filter() - 查询Users中age在 45~50之间的人的信息 - between 45 and 50
    # users=db.session.query(Users).filter(Users.age.between(45,50)).all()
    #
    # print(type(users))
    #
    # for u in users:
    #     print("ID:%d,姓名:%s,年龄:%d,邮箱:%s" % (u.id,u.username,u.age,u.email))



    ###########
    # filter_by()
    ##########
    #查询id为1的users的信息
    # user = db.session.query(Users).filter_by(id=1).first()
    # print(user)

    ##########
    # 查询 users 表中的前2条数据
    #########
    # users = db.session.query(Users).limit(2).all()

    # 获取users表中过滤前3条数据后剩余的前2条数据
    # users = db.session.query(Users).limit(2).offset(3).all()


    ###########
    # 先按照年龄降序排序,再按照id升序排序
    ##########
    # users = db.session.query(Users).order_by("age desc,id asc").all()

    ##########
    # 分组查询 - group_by
    #########
    # users = db.session.query(Users.age).group_by('age').all()
    #
    # print(users)

    #########
    # 聚合函数-avg()
    #########
    # result=db.session.query(func.avg(Users.age).label('avgAge')).first()

    # 按年龄进行分组,求组内的年龄的平均值
    # result=db.session.query(Users.age,func.avg(Users.age),func.sum(Users.age)).group_by('age').all()
    # print(result)

    ###########
    # 基于Models进行的查询
    ##########
    # users = Users.query.all()
    # users = Users.query.filter(Users.id > 1).all()
    users = Users.query.filter_by(id=3).all()
    for u in users:
        print("ID:%d,姓名:%s,年龄:%d,邮箱:%s" % (u.id,u.username,u.age,u.email))

    return "<script>alert('Query OK');</script>"

@app.route('/04-queryall')
def queryall():
    users = Users.query.all()
    return render_template('04-queryall.html',users = users)


@app.route('/05-update')
def update_views():
    #接收前端传递过来的参数 id
    id = request.args.get('id')
    #根据id查询出对应的对象
    user=Users.query.filter_by(id=id).first()
    #将查询出来的对象发送到05-update.html中进行显示
    return render_template('05-update.html',user=user)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')