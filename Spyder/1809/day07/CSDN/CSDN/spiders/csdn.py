# -*- coding: utf-8 -*-
import scrapy
# 第二步
from CSDN.items import CsdnItem


class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['blog.csdn.net']
    start_urls = ['https://blog.csdn.net/cpongo4/article/details/86613730']

    def parse(self, response):
        # 第四步：创建项目对象，赋值
        item = CsdnItem()
        title_xpath = "//h1[@class='title-article']/text()"
        item['title'] = response.xpath(title_xpath).extract()[0]
        time_xpath = "//div/span[@class='time']/text()"
        item['time'] = response.xpath(time_xpath).extract()[0]
        reader_xpath = "//div/span[@class='read-count']/text()"
        item['reader'] = response.xpath(reader_xpath).extract()[0]
        article_xpath = "//div/div[@class='show-content-free']"
        item['article'] = response.xpath(article_xpath).extract()[0]

        yield item
