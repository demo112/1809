# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from .settings import *

class TencentworkPipeline(object):
    def process_item(self, item, spider):
        print(item['tx_work'])
        print(item['tx_kind'])
        print(item['tx_inneed'])
        print(item['tx_position'])
        print(item['tx_time'])
        print(item['tx_link'])
        return item


class TencentMongoPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
        self.db = self.conn[MONGO_DATABASE]
        self.myset = self.db[MONGO_SET]
        pass

    def process_item(self, item, spider):
        d = dict(item)
        self.myset.insert_one(d)
        return item

    def close_spider(self, spider):
        print('执行close_spider函数')
