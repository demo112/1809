import time
import pymysql
import requests
import json
from user_agent import UserAgent


class DoubanSpider(object):
    def __init__(self):
        self.params = {}
        self.base_url = 'https://movie.douban.com/j/chart/top_list?'
        self.headers = user_agent.choice_headers()
        self.proxies = user_agent.choice_ip()
        # 连接数据库
        self.db = pymysql.connect('127.0.0.1', 'root', '123456', 'doubandb', charset='utf8')
        self.cursor = self.db.cursor()

    def work_on(self):
        print("\033[31m***************************\033[0m")
        print("\033[32m******剧情|喜剧|爱情*********\033[0m")
        print("\033[32m***************************\033[0m")
        print("\033[31m***************************\033[0m")
        kinds = ['剧情', '喜剧', '爱情']
        kind = input('请输入电影类型')
        kind_dic = {
            '剧情': 11,
            '喜剧': 5,
            '爱情': 13
        }
        if kind in kinds:
            n = input("请输入爬取电影的数量")
            start = input('请输入开始')
            film_type = kind_dic[kind]
            print(film_type)
            self.params = {
                'type': film_type,
                'interval_id': '100:90',
                'action': '',
                'start': start,
                'limit': n
            }
            self.get_page()
            print('爬取成功， 数量%s', n)
        else:
            print("您输入的选项不存在")
            self.work_on()

    def get_page(self):
        url = self.base_url
        res = requests.get(url, headers=self.headers, params=self.params)
        res.encoding = 'utf-8'
        html = res.text
        self.parse_page(html)

    def parse_page(self, html):
        # change json html to list
        html_list = json.loads(html)
        for h_dic in html_list:
            name = h_dic['title']
            score = float(h_dic['score'].strip())
            actors = ','.join(h_dic['actors'])
            L = [name, score, actors]
            self.write_to_mysql(L)

    def write_to_mysql(self, info_list):
        ins = 'insert into film(name, score, actors)values(%s, %s, %s)'
        self.cursor.execute(ins, info_list)
        self.db.commit()


if __name__ == '__main__':
    user_agent = UserAgent()
    start_time = time.time()
    douban = DoubanSpider()
    douban.work_on()
    end_time = time.time()
    times = end_time - start_time
    print('执行时间：%.2f' % times)
