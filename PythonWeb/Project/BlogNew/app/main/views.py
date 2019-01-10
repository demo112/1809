"""处理main业务中的路由和视图处理函数"""

from . import main
from .. import db
from .. import models


@main.route('/')
def main_index():
    return "这是main应用中的首页程序"
