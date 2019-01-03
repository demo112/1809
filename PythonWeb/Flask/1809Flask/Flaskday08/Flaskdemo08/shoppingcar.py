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


class Buyer(db.Model):
    __tablename__ = 'buyer'
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(30))
    uemail = db.Column(db.String(300))

    def __repr__(self):
        return "<Buyer:%r>" % self.uname


class Goods(db.Model):
    __tablename__ = 'goods'
    id = db.Column(db.Integer, primary_key=True)
    gname = db.Column(db.String(200), unique=True)
    gprice = db.Column(db.Float)
    users = db.relationship(
        "Buyer",
        backref=db.backref('goods', lazy='dynamic'),
        lazy='dynamic',
        secondary='shoppingcar'
    )


class ShoppingCar(db.Model):
    __tablename__ = 'shoppingcar'
    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey("buyer.id"))
    goods_id = db.Column(db.Integer, db.ForeignKey("goods.id"))
    count = db.Column(db.Integer, default=1)


db.create_all()


@app.route('/adduser')
def adduser():
    buyer = Buyer()
    buyer.uname = '屈亚伟'
    buyer.uage = 19
    db.session.add(buyer)
    return "添加成功"


@app.route('/addgoods')
def addgoods():
    goods = Goods()
    goods.gname = 'iPhone XS'
    goods.gprice = 8888
    db.session.add(goods)


@app.route('/reqcar')
def reqcar():
    buyer = Buyer.query.filter(id=1).first()
    goods = buyer.goods.all()
    for i in goods:
        print(i.gname)
        print(i.gprice)


@app.route('/14-regstudent')
def regstudent():
    buyer = Buyer.query.filter_by(id=4).first()
    good = Goods.query.filter_by(id=1).first()
    buyer.goods.append(good)
    return "增加关联数据成功"


if __name__ == '__main__':
    manager.run()
