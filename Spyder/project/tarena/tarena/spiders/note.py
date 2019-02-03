# -*- coding: utf-8 -*-
import scrapy


class NoteSpider(scrapy.Spider):
    name = 'note'
    allowed_domains = ['code.tarena.com']
    start_urls = ['http://code.tarena.com/']

    def parse(self, response):
        pass
