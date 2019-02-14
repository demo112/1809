# -*- coding: utf-8 -*-
import json

import scrapy
import urllib.parse
from So360.items import *

class So360Spider(scrapy.Spider):
    name = 'so360'
    allowed_domains = ['image.so.com']
    start_urls = ['http://image.so.com/']

    def parse(self, response):
        pass

    def start_requests(self):
        """重写方法，自己指定起始的URL地址"""
        # 拼接url地址并发给调度器
        base_url = 'http://image.so.com/zj?'
        for page in range(10):
            sn = page * 30
            params = {
                'ch': 'beauty',
                'sn': str(sn),
                'listtype': 'new',
                'temp': '1'
            }
            params = urllib.parse.urlencode(params)
            url = base_url + params
            yield scrapy.Request(url, callback=self.parse_image)

    def parse_image(self, response):
        item = So360Item()
        html = response.text
        img_dict = json.loads(html)
        for img in img_dict['list']:
            item['imglink'] = img['qhimg_url']
            yield item
