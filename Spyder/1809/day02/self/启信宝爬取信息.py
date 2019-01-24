import random
import re
import ssl
import time
import urllib.request
from csv import writer
import pymongo
import pymysql
import warnings
from userAgent import headers

ssl._create_default_https_context = ssl._create_unverified_context


class MaoYan(object):
    def __init__(self):
        # self.keyword = input('输入您需要的关键词')
        self.keyword = urllib.parse.urlencode({'key': '山东'})
        self.start = int(input('起始页数（默认第一页）') or 1)
        self.stop = int(input('结束页数（默认第十页）') or 3) + 1
        self.sleep_time = random.randrange(1, 3)
        self.BASE_URL = 'https://www.qixin.com/search?'
        warnings.filterwarnings('ignore')
        self.mysql_db = pymysql.connect('127.0.0.1', 'root', '123456', 'maoyandb', charset='utf8')
        self.cursor = self.mysql_db.cursor()
        self.data = {

        }

    def get_page(self, url):
        """获取页面"""
        req = urllib.request.Request(url, headers=headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')
        print(html)
        self.parse_page(html)

    def parse_page(self, html):
        """解析页面"""
        # r_p = re.compile('<div class="movie-item-info">.*?'
        #                'title="(.*?)" data-act.*?'
        #                '<p class="star">(.*?)</p>.*?'
        #                'class="releasetime">(.*?)</p>.*?', re.S)
        every_company = re.compile('<div class="company-title">'
                                   , re.S)
        r_list = every_company.findall(html)
        print(r_list)
        # 保存到文件
        # self.save_page(r_list)
        return r_list


    def save_page(self, r_list):
        """保存到csv文件"""
        with open('Top100.csv', 'a', newline='', encoding='gb18030') as f:
            # 创建写入对象
            write = writer(f)
            for rt in r_list:
                # info = list(rt)
                info = [
                    rt[0].strip(),
                    rt[1].strip(),
                    rt[2].strip(),
                ]
                # 利用写入对象的方法写入列表
                write.writerow(info)

    def write_mongo(self, r_list):
        DATABASE = '待确定'
        TABLE = '待确定'
        # 链接对象
        self.conn = pymongo.MongoClient('127.0.0.1', 27017)
        # 数据库对象
        db = self.conn[DATABASE]
        # 数据表对象
        self.myset = db[TABLE]
        for rt in r_list:
            dic = dict(name=rt[0].strip(), star=rt[1].strip(), date=rt[2].strip())
            self.myset.insert_one(dic)

    def write_mysql(self, r_list):
        ins = 'insert into top100(name, star, time) values(%s, %s, %s)'
        for rt in r_list:
            print(rt)
            L = [
                rt[0].strip(),
                rt[1].strip(),
                rt[2].strip()
            ]
            # 使用列表传参
            self.cursor.execute(ins, L)
            self.mysql_db.commit()


    def work_on(self):
        for pg in range(self.start, self.stop):
            time.sleep(self.sleep_time)
            url = self.BASE_URL + self.keyword + '&page=' + str(pg)
            # print(url)
            self.get_page(url)
        self.cursor.close()
        self.mysql_db.close()


if __name__ == '__main__':
    maoyan = MaoYan()
    maoyan.work_on()
