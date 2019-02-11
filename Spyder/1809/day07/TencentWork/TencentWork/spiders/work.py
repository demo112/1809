# -*- coding: utf-8 -*-
import scrapy
from ..items import *


class WorkSpider(scrapy.Spider):
    name = 'work'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?start=']

    def parse(self, response):
        for page in range(0, 2858, 10):
            full_url = self.start_urls[0] + str(page)
            yield scrapy.Request(full_url, callback=self.parseHtml)

    def parseHtml(self, response):
        item = TencentworkItem()
        # 职位名称
        work_xpath = "./td/a/text()"
        # 类别
        kind_xpath = "./td[2]/text()"
        # 招聘人数
        inneed_xpath = "./td[3]/text()"
        # 招聘地点
        position_xpath = "./td[4]/text()"
        # 发布时间
        time_xpath = "./td[5]/text()"
        # 职位链接
        link_xpath = "./td[1]/a/@href"

        base_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        for base in base_list:
            # 职位名称
            item['tx_work'] = base.xpath(work_xpath).extract()
            if item['tx_work']:
                item['tx_work'] = item['tx_work'][0]
            else:
                item['tx_work'] = '无'
            # 类别
            item['tx_kind'] = base.xpath(kind_xpath).extract()
            if item['tx_kind']:
                item['tx_kind'] = item['tx_kind'][0]
            else:
                item['tx_kind'] = '无'
            # 招聘人数
            item['tx_inneed'] = base.xpath(inneed_xpath).extract()
            if item['tx_inneed']:
                item['tx_inneed'] = item['tx_inneed'][0]
            else:
                item['tx_inneed'] = '无'
            # 招聘地点
            item['tx_position'] = base.xpath(position_xpath).extract()
            if item['tx_position']:
                item['tx_position'] = item['tx_position'][0]
            else:
                item['tx_position'] = '无'
            # 发布时间
            item['tx_time'] = base.xpath(time_xpath).extract()
            if item['tx_time']:
                item['tx_time'] = item['tx_time'][0]
            else:
                item['tx_time'] = '无'
            # 职位链接
            item['tx_link'] = base.xpath(link_xpath).extract()
            if item['tx_link']:
                item['tx_link'] = item['tx_link'][0]
            else:
                item['tx_link'] = '无'

            yield item
