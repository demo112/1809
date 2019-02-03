import requests
import pymongo
from lxml import etree
from user_agent import UserAgent


user_agent = UserAgent()


class Qiushibaike(object):
    def __init__(self):
        self.base_url = 'https://www.qiushibaike.com/text/'
        self.headers = user_agent.choice_headers()
        self.conn = pymongo.MongoClient('127.0.0.1', 27017)
        self.db = self.conn['qiushidb']
        self.myset = self.db['text']

    def work_on(self):
        self.change_page()

    def change_page(self):
        self.get_page()

    def get_page(self):
        # 请求url，获取页面
        res = requests.get(self.base_url, headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        self.parse_page(html)

    def parse_page(self, html):
        """获取div对象，进行下一步解析"""
        xpath = '//div[contains(@id, "qiushi_tag_")]'
        parse_html = etree.HTML(html)
        div_list = parse_html.xpath(xpath)
        print(div_list)
        for div in div_list:
            print(div)
            self.parse_info(div)
        self.save_page()

    def parse_info(self, div):
        # 用户名: './div/a/h2'
        name = div.xpath('./div/a/h2')
        if not name:
            name = "匿名用户"
        else:
            name = name[0].text.strip()
        # 段子内容: './/div[@class="content"]/span'
        content = div.xpath('.//div[@class="content"]/span')
        if not content:
            content = '空'
        else:
            content = content[0].text.strip()
        # 好笑数量: './/i[@class="number")]'
        laugh_num = div.xpath('.//i[@class="number"]')
        if not laugh_num:
            laugh_num = 0
        else:
            laugh_num = int(laugh_num[0].text)
        # 评论数量: './/i[@class="stats-comments")]'
        talk_num = div.xpath('.//i[@class="number"]')
        if not talk_num:
            talk_num = 0
        else:
            talk_num = int(talk_num[1].text)
        dic = {
            'name': name,
            'content': content,
            'laugh_num': laugh_num,
            'talk_num': talk_num
        }
        self.myset.insert_one(dic)
        # print(name, content, laugh_num)
        # print(name, content, laugh_num, talk_num, dic)

    def save_page(self):
        pass

    def save_mongo(self):
        pass


if __name__ == '__main__':
    qiushi = Qiushibaike()
    qiushi.work_on()
