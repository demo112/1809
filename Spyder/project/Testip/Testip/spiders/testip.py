# -*- coding: utf-8 -*-
import copy
import time

import scrapy
import urllib.parse
from ..items import *

class TestipSpider(scrapy.Spider):
    name = 'testip'
    allowed_domains = ['www.kuaidaili.com/free/inha/']
    # start_urls = [
    #     'http://www.kuaidaili.com/free/inha/1',
    #     'http://www.kuaidaili.com/free/inha/2',
    #     'http://www.kuaidaili.com/free/inha/3',
    # ]

    # def parse(self, response):
    #     print('parse', response.url)
    #     return self.work_on

    def start_requests(self):
        base_url = 'https://www.kuaidaili.com/free/inha/'
        start = int(input("请输入起始页面"))
        stop = int(input("请输入结束页面")) + 1
        url_list = []
        m = 0
        for n in range(start, stop):
            url = base_url + str(n) + '/'
            url_list.append(url)
        # print(url_list)
        for url in url_list:
            print(url)
            yield scrapy.Request(url, callback=self.work_on)

    def work_on(self, response):
        # print('work_on', response.url)
        for i in range(15):
            item = TestipItem()
            i =  i + 1
            ip_xpath = '//table/tbody/tr[%s]/td[1]/text()' % i
            ip = response.xpath(ip_xpath).extract()[0]
            port_xpath = '//table/tbody/tr[%s]/td[2]/text()' % i
            port = response.xpath(port_xpath).extract()[0]
            item['proxy'] = str(ip) + ':' + str(port)
            # print(ip, port)
            # print(item['proxy'])
            yield item
