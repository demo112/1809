import json

from flask import Flask, request, render_template, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from raven.utils.stacks import to_dict

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@127.0.0.1:3306/login_guoyuan"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'you guess'
db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(50), nullable=False)
    upwd = db.Column(db.String(200), nullable=False)
    nickname = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        dic = {
            "id": self.id,
            "uname": self.uname,
            "nickname": self.nickname,
            "upwd": self.upwd
        }
        return dic


@app.route('/04-json')
def json_make():
    # dic = {
    #     'name': 'lv',
    #     'height': '177',
    #     'weight': '90',
    #     'hobby': 'female',
    # }
    # jsonStr = json.dumps(dic)

    # lis = [
    #     {
    #         'name': 'lv',
    #         'height': '177',
    #         'weight': '90',
    #         'hobby': 'female',
    #     },
    #     {
    #         'name': 'wang',
    #         'height': '170',
    #         'weight': '80',
    #         'hobby': 'female',
    #     },
    #     {
    #         'name': 'meng',
    #         'height': '167',
    #         'weight': '50',
    #         'hobby': 'male',
    #     },
    #     {
    #         'name': 'wei',
    #         'height': '180',
    #         'weight': '70',
    #         'hobby': 'female',
    #     },
    # ]
    users = User.query.all()
    lis = to_dict([x for x in users])
    # 自定义方法：将对象的所有属性封装到一个字典
    jsonStr = json.dumps(lis)
    return jsonStr


if __name__ == '__main__':
    app.run(debug=True)
