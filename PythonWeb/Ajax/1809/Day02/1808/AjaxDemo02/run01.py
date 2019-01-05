from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:123456@localhost:3306/flask"
db = SQLAlchemy(app)

class Login(db.Model):
    __tablename__ = "login"
    id = db.Column(db.Integer,primary_key=True)
    lname = db.Column(db.String(30))
    lpwd = db.Column(db.String(30))
    uname = db.Column(db.String(30))

    def to_dict(self):
        dic = {
            'id':self.id,
            'lname' : self.lname,
            'lpwd' : self.lpwd,
            'uname' : self.uname,
        }
        return dic

@app.route('/00-homework')
def homework():
    return render_template('00-homework.html')

@app.route('/00-server')
def server00():
    lname = request.args.get('lname')
    login=Login.query.filter_by(lname=lname).first()
    if login:
        return "用户名称已经存在"
    else:
        return "通过"

@app.route('/01-post')
def post():
    return render_template("01-post.html")

@app.route('/01-server',methods=['POST'])
def server01():
    uname = request.form['uname']
    uage = request.form['uage']
    return "传递过来的uname的值为:%s,传递过来的uage的值为:%s" % (uname,uage)

@app.route('/02-form',methods=['GET','POST'])
def form():
    if request.method == 'GET':
        return render_template('02-form.html')
    else:
        uname = request.form['uname']
        uage = request.form['uage']
        return "传递过来的uname的值为:%s,传递过来的uage的值为:%s" % (uname,uage)

@app.route('/03-getlogin')
def getlogin():
    return render_template('03-getlogin.html')

@app.route('/03-server')
def server03():
    logins = Login.query.all()
    str1 = ""
    for login in logins:
        str1 += str(login.id)
        str1 += login.lname
        str1 += login.lpwd
        str1 += login.uname
    return str1

@app.route('/04-json')
def json_views():
    return render_template("04-json.html")

@app.route('/04-server')
def server04():
    # list = ["王老六","RapWang","隔壁老顽固"]

    # dic = {
    #     'name':'TeacherWang',
    #     'age' : 35,
    #     'gender' : 'Male',
    # }
    # jsonStr=json.dumps(dic)

    list = [
        {
            "name":"wangwc",
            "age":35,
            "gender":"Male",
        },
        {
            'name':'RapWang',
            'age':40,
            'gender':'Female',
        }
    ]
    jsonStr=json.dumps(list)
    return jsonStr

@app.route('/05-json-login')
def json_login():
    return render_template('05-json-login.html')


@app.route('/05-server')
def server05():
    #得到id为一的Login的信息
    login=Login.query.filter_by(id=1).first()
    jsonStr=json.dumps(login.to_dict())
    return jsonStr

if __name__ == "__main__":
    app.run(debug=True)