import re
import requests
import pymongo
from user_agent import UserAgent

url = 'https://www.neihan8.com/njjzw/index'
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)"}

user_agent = UserAgent()


class NeiHan(object):
    def __init__(self):
        self.base_url = 'https://www.neihan8.com/njjzw/'
        self.headers = user_agent.choice_headers()
        self.conn = pymongo.MongoClient('127.0.0.1', 27017)
        DATABASE = "neihandb"
        TABLE = 'naojin'
        db = self.conn[DATABASE]
        self.myset = db[TABLE]

    def getpage(self, now_url):
        res = requests.get(now_url, headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        self.parsepage(html)

    def parsepage(self, html):
        # print(html)
        p = re.compile('.*?class="title".*?title="(.*?)">.*?'
                       'class="desc">\s*(.*?)\s*</div>', re.S)
        r_list = p.findall(html)
        # print(r_list)
        self.writemongo(r_list)

    def writemongo(self, r_list):
        for rt in r_list:
            d = {
                'question': rt[0].strip(),
                'answer': rt[1].strip(),
            }
            self.myset.insert_one(d)
            print(d)

    def work_on(self):
        menu = """
                \033[31m********************
                \033[32m****  1.爬取   ******
                \033[32m****  2.退出   ******
                \033[31m********************
                """
        cmd = input(menu)
        if cmd.strip() == '1':
            n = input("请输入页数")
            # 判断是否是字符串形式的数字
            if n.strip().isdigit():
                n = int(n)
                if n > 1:
                    now_url = self.base_url
                    self.getpage(now_url)
                    print("第1页成功")
                    for pn in range(2, n + 1):
                        now_url = self.base_url + 'index_' + str(pn) + '.html'
                        self.getpage(now_url)
                        print("第%d页成功" % pn)
                elif n == 1:
                    now_url = self.base_url
                    self.getpage(now_url)
                    print("第1页成功")
                else:
                    print("请输入1——175的整数")
        else:
            pass


if __name__ == "__main__":
    neihan = NeiHan()
    neihan.work_on()
