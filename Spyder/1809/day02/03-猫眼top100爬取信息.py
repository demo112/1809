import random
from re import S, compile
import ssl
import time
import urllib.request
from csv import writer
import pymongo
import pymysql
import warnings

ssl._create_default_https_context = ssl._create_unverified_context


class MaoYan(object):
    def __init__(self):
        self.BASE_URL = 'https://maoyan.com/board/4?offset='
        self.USER_AGENT = [
            {'User-agent': 'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'},
            {'User-agent': 'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'},
            {'User-agent': 'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0'},
            {'User-agent': 'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)'},
            {'User-agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)'},
            {'User-agent': 'Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)'},
            {'User-agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1'},
            {'User-agent': 'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1'},
            {'User-agent': 'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11'},
            {'User-agent': 'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11'},
            {'User-agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11'},
            {'User-agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)'},
            {'User-agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)'},
            {'User-agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)'},
            {'User-agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)'},
            {'User-agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)'},
            {'User-agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)'},
            {'User-agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)'},
            {'User-agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)'},
        ]
        warnings.filterwarnings('ignore')
        self.mysql_db = pymysql.connect('127.0.0.1', 'root', '123456', 'maoyandb', charset='utf8')
        self.cursor = self.mysql_db.cursor()


    def get_page(self, url):
        """获取页面"""
        num = random.randint(0, len(self.USER_AGENT))
        headers = self.USER_AGENT[num]
        print(num)
        req = urllib.request.Request(url, headers=headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')
        self.parse_page(html)

    def parse_page(self, html):
        """解析页面"""
        r_p = compile('<div class="movie-item-info">.*?'
                       'title="(.*?)" data-act.*?'
                       '<p class="star">(.*?)</p>.*?'
                       'class="releasetime">(.*?)</p>.*?', S)
        r_list = r_p.findall(html)
        # 保存到文件
        # self.save_page(r_list)

        # 保存到mongo
        # self.write_mongo(r_list)

        # 保存到mysql
        self.write_mysql(r_list)


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
        DATABASE = 'maoyandb'
        TABLE = 'top100'
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
        for pg in range(0, 30, 10):
            time.sleep(2.3)
            url = self.BASE_URL + str(pg)
            self.get_page(url)
        self.cursor.close()
        self.mysql_db.close()


if __name__ == '__main__':
    maoyan = MaoYan()
    maoyan.work_on()
