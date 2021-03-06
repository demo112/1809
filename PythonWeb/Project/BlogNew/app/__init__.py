"""
    当前程序的初始化工作
    主要工作
    构建Flask应用实例及各种配置
    创建SQLAlchemy的应用实例
    关联蓝图（BulePrint）程序
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



# 声明SQLAlchemy的应用实例
db = SQLAlchemy()


def create_app():
    """
    创建Flask实例
    配置启动模式为调试模式
    配置数据库的连库信息，自动提交
    配置session的SECRET_KEY
    返回已创建好的Flask实例
    """
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:123456@localhost:3306/blog'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
    app.config['SECRET_KEY'] = 'bgfasdfsdfsvbewioranhgviowegobirvwnilbuesrh'
    # 关联db和app
    # 用app初始化db
    db.init_app(app)
    # 将main程序与app关联到一起
    from .main import main as main_blueprint
    from .users import user as user_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(user_blueprint)
    print(__name__)
    return app
