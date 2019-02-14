# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy

# class So360Pipeline(object):
#     def process_item(self, item, spider):
#         return item


class So360Imageline(ImagesPipeline):
    """重写scrapy的图片管道类"""
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['imglink'])
