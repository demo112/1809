from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123456@localhost:3306/login_guoyuan'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    uemail = db.Column(db.String(50), nullable=False)
    nickname = db.Column(db.String(50), nullable=False)
    uphone = db.Column(db.String(11)),
    uname = db.Column(db.String(50)),
    upwd = db.Column(db.String(200), nullable=False)
    #定义方法 - to_dict ,将当前对象中所有的属性封装到一个字典中并返回
    def to_dict(self):
        dic = {
            'id':self.id,
            'uemail':self.uemail,
            'nickname': self.nickname,
            'uphone':self.uphone,
            'uname':self.uname,
            'upwd':self.upwd,

        }
        return dic



@app.route('/01-checkuname')
def checkuname_views():
    uname=request.args['uname']
    user=User.query.filter_by(uname=uname).first()
    if user:
        return "用户名称已存在"
    else:
        return "通过"


@app.route('/02-register',methods=['POST'])
def register_views():
    #接收前端传递过来的数据
    uname=request.form['uname']
    upwd=generate_password_hash(request.form['upwd'])
    nickname=request.form['nickname']
    user = User()
    user.uname = uname
    user.upwd = upwd
    user.nickname = nickname
    try:
        db.session.add(user)
        db.session.commit()
        return "注册成功"
    except Exception as ex:
        print(ex)
        return "注册失败"


@app.route('/03-users')
def users_views():
    list=User.query.all()
    str = ""
    for u in list:
        str += u.uname+","
        str += u.upwd+","
        str += u.nickname+"|"
    return str


@app.route('/04-json')
def json_views():
    # 通过字典表示单个数据
    # dic = {
    #     'name':'TeacherLv',
    #     'height':177,
    #     'weight':90,
    #     'hobby':'Female'
    # }
    # #将dic转换为JSON格式的字符串
    # jsonStr = json.dumps(dic)
    # print(jsonStr)
    # return jsonStr

    #通过列表表示多个数据
    # list = [
    #     {
    #         'name':'TeacherLv',
    #         'heihgt':177,
    #         'weight':90,
    #         'hobby':'Female'
    #     },
    #     {
    #         'name': 'TeacherWei',
    #         'heihgt': 175,
    #         'weight': 90,
    #         'hobby': 'Game'
    #     }
    # ]
    # jsonStr=json.dumps(list)
    # return jsonStr

    #从数据库中读取user表中所有的数据并转换为json字符串
    users=User.query.all()
    list = []
    for user in users:
        list.append(user.to_dict())
    return json.dumps(list)


@app.route('/05-users')
def users1():
    # 查询user 表中的所有数据
    users = User.query.all()
    # 将查询结果转换为json字符串并响应
    list = []
    # 创建一个空列表
    for u in users:
        list.append(u.to_dict())
    # 循环便利，并调用to_dict转换为字典添加进列表
    # 响应
    return json.dumps(list)


if __name__ == "__main__":
    app.run(debug=True)
