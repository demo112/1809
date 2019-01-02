from flask import *
from flask_sqlalchemy import SQLAlchemy
# import pymysql
# pymysql.install_as_MySQLdb()
# 1.通过 app (Flask应用实例) 构建配置信息
app = Flask(__name__)
# 指定数据库的配置给app
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 将app交给SQLAlchemy，创建数据库实例
db = SQLAlchemy(app)


# 创建实体类Users
class Users(db.Model):
    # 映射到数据库中表名叫users
    __tablename__ = 'users'
    # 创建字段：id 主键，自增
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 创建字段：username 长度为80的字符串，不允许为空，值唯一
    username = db.Column(db.String(80), nullable=False, unique=True)
    # 创建字段：age 整数 允许为空
    age = db.Column(db.Integer, nullable=True)
    # 创建字段：email 长度200的字符串 唯一
    email = db.Column(db.String(200), unique=True)
    # 创建字段：birth Date格式
    birth = db.Column(db.Date)
    # 创建字段：isActive 布尔类型 默认值为True
    isActive = db.Column(db.Boolean, default=False)


# 将创建好的实体类映射回数据库
db.create_all()


@app.route('/', methods=['GET', "POST"])
def file_views():
    print(db)
    return '访问成功'


if __name__ == "__main__":
    app.run(debug=True)
