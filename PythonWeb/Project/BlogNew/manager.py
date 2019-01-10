"""
管理和启项目
通过manager（）对象管理项目，并添加数据迁移的指令
"""
from .app import create_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from .app.models import *


app = create_app()
# db和app的绑定逻辑
# 先创建db（无app初始化），
# 创建app，将db初始化后返回app，
# 这样db和app就是关联的
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
