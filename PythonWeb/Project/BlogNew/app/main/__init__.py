"""main处理与博客相关的业务逻辑"""
# 主要处理业务相关逻辑（发表博客，查看删除……）
# 将自己加入到蓝图中
from flask import Blueprint
# 绑定当前程序包的名称
main = Blueprint('main', __name__)
from . import views
