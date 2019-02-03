import csv

import pymongo

import requests
from lxml import etree

from user_agent import UserAgent


class LianJia(object):
    def __init__(self):
        self.city = input("请输入您所在的城市")
        self.base_url = 'https://%s.lianjia.com/ershoufang/' % self.city
        self.header = user_agent.choice_headers()
        self.proxies = user_agent.choice_ip()
        self.url = self.check_city()
        self.ip = ''
        self.proxies = {"http": "http://" + self.ip}

    def work_on(self):
        """分析链接及请求需求"""
        # https: // jn.lianjia.com / ershoufang /
        # https: // jn.lianjia.com / ershoufang / pg2 /
        # https: // jn.lianjia.com / ershoufang / pg3 /
        self.get_url()
        pass

    def get_url(self):
        """获取请求，请求到每个城市的二手房主页，并根据要求获取每个子页面的链接"""
        back_url = self.url
        print("获取网页", self.url)
        start = int(input("请输入开始页面"))
        stop = int(input("请输入结束页面"))
        for pg in range(start, stop + 1):
            if pg == 1:
                pass
            else:
                self.url = self.url + 'pg' + str(pg) + '/'
            self.get_each_page()
            self.url = back_url

    def get_each_page(self):
        """针对页面链接进行，获取"""
        # print(url)
        res = requests.get(self.url, headers=self.header, proxies=self.proxies)
        res.encoding = 'utf-8'
        html = res.text
        print(self.url)
        # self.save_page(html)
        self.parse_page(html)

    def save_page(self, html):
        """根据获取到的html解析内容，将其保存为本地文件"""
        filename = self.url.split('/')[-2] + '.html'
        with open(filename, 'w') as f:
            f.write(html)

    def check_city(self):
        """
        检查城市输入是否有请求内容
        """
        url = self.base_url
        res = requests.get(url=url, headers=self.header)
        if res.status_code == 200:
            return url
        else:
            print('已返回首页')
            return 'https://www.lianjia.com/city/'

    def parse_page(self, html):
        """解析出每条信息的对象"""
        xpath = '//ul[@class="sellListContent"]/li[@class="clear LOGCLICKDATA"]'
        prase_ershou = etree.HTML(html)
        house_list = prase_ershou.xpath(xpath)
        # print(house_list)
        self.info_list(house_list)

    def info_list(self, house_list):
        info_list = []
        for house in house_list:
            # print(house)
            # 简介
            xpath_title = './div[@class="info clear"]/div[@class="title"]/a/text()'
            jianjie = house.xpath(xpath_title)
            # 小区名
            xpath_name = './div[@class="info clear"]/div[@class="address"]/div[@class="houseInfo"]/a/text()'
            name = house.xpath(xpath_name)
            # 户型
            xpath_style = './div[@class="info clear"]/div[@class="address"]/div[@class="houseInfo"]/text()'
            style = house.xpath(xpath_style)
            # 楼型
            xpath_buiding = './div[@class="info clear"]/div[@class="flood"]/div[@class="positionInfo"]/text()'
            buiding = house.xpath(xpath_buiding)
            # 地址
            xpath_address = './div[@class="info clear"]/div[@class="flood"]/div[@class="positionInfo"]/a/text()'
            address = house.xpath(xpath_address)
            # 热度
            xpath_hot = './div[@class="info clear"]/div[@class="followInfo"]/text()'
            hot = house.xpath(xpath_hot)
            # tag1
            xpath_tag1 = './div[@class="info clear"]/div[@class="tag"]/span[@class="vr"]/text()'
            tag1 = house.xpath(xpath_tag1)
            # tag2
            xpath_tag2 = './div[@class="info clear"]/div[@class="tag"]/span[@class="taxfree"]/text()'
            tag2 = house.xpath(xpath_tag2)
            # tag3
            xpath_tag3 = './div[@class="info clear"]/div[@class="tag"]/span[@class="haskey"]/text()'
            tag3 = house.xpath(xpath_tag3)
            # priceInfo
            xpath_priceInfo = './div[@class="info clear"]/div[@class="priceInfo"]/div/span/text()'
            priceInfo = house.xpath(xpath_priceInfo)

            info = [
                jianjie,
                name,
                style,
                buiding,
                address,
                hot,
                tag1,
                tag2,
                tag3,
                priceInfo
            ]
            print(info)
            info_list.append(info)
            # self.save_mongo()
        self.save_csv(info_list)

    # def save_mongo(self):
    #     conn_mongo = pymongo.MongoClient('127.0.0.1', 27017)
    #     db = conn_mongo['lianjiadb']
    #     myset = db['house_info']
    #     myset.insert_one()

    def save_csv(self, info_list):
        filename = self.city + '二手房信息.csv'
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['小区名', '户型', '楼型', '地址', '热度', 'tag1', 'tag2', 'tag3', 'priceInfo'])
            for info in info_list:
                writer.writerow(info)


if __name__ == '__main__':
    user_agent = UserAgent()
    chaxun = LianJia()
    chaxun.work_on()
