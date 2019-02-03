# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from .settings import *

class TencentworkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 职位名称
    tx_work = scrapy.Field()
    # 类别
    tx_kind = scrapy.Field()
    # 招聘人数
    tx_inneed = scrapy.Field()
    # 招聘地点
    tx_position = scrapy.Field()
    # 发布时间
    tx_time = scrapy.Field()
    # 职位链接
    tx_link = scrapy.Field()
    pass
