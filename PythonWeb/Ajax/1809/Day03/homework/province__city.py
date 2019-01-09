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


class Province(db.Model):
    __tablename__ = "province"
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(30))
    cites = db.relationship('City', backref='province', lazy='dynamic')

    def to_dict(self):
        dic = {
            'id': self.id,
            'pname': self.pname
        }
        return dic


class City(db.Model):
    __tablename__ = "city"
    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.Integer, db.ForeignKey('province.id'))
    cname = db.Column(db.String(30))

    def to_dict(self):
        dic = {
            'id': self.id,
            'pid': self.pid,
            'cname': self.cname

        }
        return dic


db.create_all()


@app.route('/05-loadpro')
def loadpro():
    # 获取province表中所有数据，并构建成json字符串
    provinces = Province.query.all()
    lis = []
    for p in provinces:
        lis.append(p.to_dict())
    return json.dumps(lis)


@app.route('/06-loadcity')
def loadcity():
    pid = request.args['pid']
    # 获取province表中所有数据，并构建成json字符串
    # way1
    # pro = Province.query.filter_by(id=pid).first()
    # cities = pro.cities
    # way2kl
    cities = City.query.filter_by(pid=pid).all()
    lis = []
    for p in cities:
        lis.append(p.to_dict())
    return json.dumps(lis)


if __name__ == '__main__':
    manager.run()
