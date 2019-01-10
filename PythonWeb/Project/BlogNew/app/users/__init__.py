# 与用户业务相关的操作
# 用户的注册，登陆，登出
from flask import Blueprint
user = Blueprint('user', __name__)
from . import views
