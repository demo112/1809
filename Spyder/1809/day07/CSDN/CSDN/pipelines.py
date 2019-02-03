# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import pymysql
from .settings import *


class CsdnPipeline(object):
    def process_item(self, item, spider):
        # 第五部：处理数据
        print('===================================')
        print(item['title'])
        print(item['time'])
        print(item['reader'])
        return item


class CsdnMongoPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
        self.db = self.conn[MONGO_DB]
        self.myset = self.db[MONGO_SET]

    def process_item(self, item, spider):
        # 第五部：处理数据
        dic = dict(item)
        self.myset.insert_one(dic)
        return item


class CsdnMysqlPipeline(object):
    def __init__(self):
        self.db = pymysql.connect(MYSQL_HOST,
                                  MYSQL_USER,
                                  MYSQL_PASSWORD,
                                  MYSQL_DB,
                                  charset='utf8')
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        # 第五部：处理数据
        ins = 'insert into article_info values(%s, %s, %s)'
        L = [
            item['title'],
            item['time'],
            item['reader']
        ]
        self.cursor.execute(ins, L)
        self.db.commit()
        return item

    def close_spider(self, spider):
        """
        重写scrapy方法可以做一些收尾工作
        参数必须加上spider
        """
        self.cursor.close()
        self.db.close()
