import pymongo
# 创建链接对象
print(11)

DATEBASE_NAME = 'spiderdb'
TABLE_NAME = 't1'

conn = pymongo.MongoClient('127.0.0.1', 27017)
# 创建库对象
# db = conn.spiderdb
# 使用变量创建数据库
db = conn[DATEBASE_NAME]
# 创建集合对象
# myset = db.t1
# 使用变量创建数据表
myset = db[TABLE_NAME]
# 插入文档
myset.insert_one({"name": 'Lucy'})
# mongo
# show dbs
# use spiderdb
# show collections
# db.t1.find().pretty()
# db.dropDatabase()
