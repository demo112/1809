# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CsdnItem(scrapy.Item):
    # define the fields for your item here like:
    # 第一步
    title = scrapy.Field()
    time = scrapy.Field()
    reader = scrapy.Field()
    article = scrapy.Field()
    pass
