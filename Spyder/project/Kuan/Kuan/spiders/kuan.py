# -*- coding: utf-8 -*-
import re
import scrapy
from ..items import *


class KuanSpider(scrapy.Spider):
    name = 'kuan'
    allowed_domains = ['www.coolapk.com']
    start_urls = ['http://www.coolapk.com/']
    print(0)
    def parse(self, response):
        content_list = response.xpath("//div[@class='app_left_list']/a")
        print(len(content_list))
        for content in content_list:
            print(1)
            url = content.xpath('./a/@href').extract()[0]
            print(url)
            url = response.urljoin(url)  # 拼接相对 url 为绝对 url
            yield scrapy.Request(url, callback=self.parse_url)

    def parse_url(self, response):
        item = KuanItem()
        print(2)
        item['name'] = response.css('.detail_app_title::text').extract_first()
        results = self.get_comment(response)
        item['volume'] = results[0]
        item['download'] = results[1]
        item['follow'] = results[2]
        item['comment'] = results[3]
        item['tags'] = self.get_tags(response)
        item['score'] = response.css('.rank_num::text').extract_first()
        num_score = response.css('.apk_rank_p1::text').extract_first()
        item['num_score'] = re.search('共(.*?)个评分', num_score).group(1)
        yield item

    def get_comment(self, response):
        messages = response.css('.apk_topba_message::text').extract_first()
        result = re.findall(r'\s+(.*?)\s+/\s+(.*?)下载\s+/\s+(.*?)人关注\s+/\s+(.*?)个评论.*?', messages)  # \s+ 表示匹配任意空白字符一次以上
        print('1', result)
        if result:  # 不为空
            results = list(result[0])  # 提取出list 中第一个元素
            return results

    def get_tags(self, response):
        data = response.css('.apk_left_span2')
        tags = [item.css('::text').extract_first() for item in data]
        return tags
