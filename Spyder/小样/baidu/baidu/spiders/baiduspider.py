# -*- coding: utf-8 -*-
import scrapy


class BaiduspiderSpider(scrapy.Spider):
    # 爬虫名称
    name = 'baiduspider'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
