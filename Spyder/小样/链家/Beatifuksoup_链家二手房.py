import requests
import pymongo
from bs4 import BeautifulSoup
from user_agent import UserAgent


class Lianjia(object):
    def __init__(self):
        user_agent = UserAgent()
        self.base_url = 'https://jn.lianjia.com/ershoufang/'
        self.headers = user_agent.choice_headers()
        self.proxies = {'http': 'http://' + user_agent.choice_ip()}
        self.conn = pymongo.MongoClient('127.0.0.1', 27017)
        self.db =self.conn['lianjiadb']
        self.myset = self.db['house_info']

    def work_on(self):
        url = self.base_url
        self.get_page(url)

    def get_page(self, url):
        self.url = url
        res = requests.get(self.url, headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        self.parse_page(html)
        pass

    def parse_page(self, html):
        soup = BeautifulSoup(html, 'lxml')
        house_list = soup.find_all('li', {'class': 'clear LOGCLICKDATA'})
        # print(house_list)
        for house in house_list:
            house_info = house.find('div', attrs={'class': 'info clear'}).get_text().split('|')
            print('*'*100)
            print(house_info)
            name = house_info[0].strip()
            kind = house_info[1].strip()
            size = house_info[2].strip()

            address = house.find('div', {'class': 'positionInfo'}).get_text().split('-')
            floor = (address[0].split(')')[0] + ')').strip()
            age = address[0].split(')')[1].strip()
            road =address[1].strip()
            print(floor)
            print(age)
            print(road)

            price = house.find('div', attrs={'class': 'totalPrice'}).span.string
            unit_price = house.find('div', attrs={'class': 'unitPrice'}).span.string[2:][:-4]
            print(price)
            print(unit_price)

            dic = {
                '名称': name,
                '户型': kind,
                '面积': size,
                '楼层': floor,
                '年份': age,
                '地点': road,
                '总价': price,
                '单价': unit_price
            }
            self.myset.insert_one(dic)


if __name__ == '__main__':
    lianjia = Lianjia()
    lianjia.work_on()
