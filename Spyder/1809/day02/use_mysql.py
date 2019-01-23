import warnings

import pymysql


# 创建数据库连接对象
db = pymysql.connect('localhost', 'root', '123456', charset='utf8')
# 创建游标对象
cursor = db.cursor()
# 利用游标对象的execute()方法执行命令
cdb = 'create database if not exists spider'
udb = 'use spider'
ctab = 'create table if not exists t1(id int)'
ins = 'insert into t1 values(1)'
# 过滤警告
warnings.filterwarnings('ignore')
# 提交到数据库执行
cursor.execute(cdb)
cursor.execute(udb)
cursor.execute(ctab)
cursor.execute(ins)
db.commit()

# 关闭游标
cursor.close()
# 断开数据库连接
db.close()
