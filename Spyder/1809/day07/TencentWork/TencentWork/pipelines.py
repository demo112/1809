# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TencentworkPipeline(object):
    def process_item(self, item, spider):
        print(item['tx_work'])
        print(item['tx_kind'])
        print(item['tx_inneed'])
        print(item['tx_position'])
        print(item['tx_time'])
        print(item['tx_link'])
        return item
