"""处理users相关的路由和视图处理函数"""
from . import user
from .. import db
from .. import models

@user.route('/user_index')
def user_index():
    return "这是user 里的"