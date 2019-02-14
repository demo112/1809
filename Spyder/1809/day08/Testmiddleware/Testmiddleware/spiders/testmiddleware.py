# -*- coding: utf-8 -*-
import scrapy


class TestmiddlewareSpider(scrapy.Spider):
    name = 'testmiddleware'
    allowed_domains = ['www.baidu.com']
    # start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print('这是parse函数的输出')
        pass

    def start_requests(self):
        print("请求已发出")
        yield scrapy.Request('http://www.baidu.com/')
        pass