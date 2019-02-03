import time
import urllib
import requests
import json
from multiprocessing import Queue
from threading import Thread
from user_agent import UserAgent


class XiaoMiSpider(object):
    def __init__(self):
        self.start = int(input("请输入起始页面")) - 1
        self.stop = int(input("请输入结束页面"))
        self.type = '2'
        user_agent = UserAgent()
        self.base_url = 'http://app.mi.com/categotyAllListApi?'
        self.headers = user_agent.choice_headers()
        self.proxies = {'http': 'http://' + user_agent.choice_ip()}
        self.url_queue = Queue()
        self.parse_queue = Queue()
        pass

    def work_on(self):
        # 添加url进入队列
        self.put_url_to_queue()
        # time.sleep(1)
        # 创建多个采集线程
        # all_list = []
        get_html_list = []
        parse_list = []
        # 存放所有采集线程的列表
        for i in range(10):
            t = Thread(target=self.get_html_to_queue)
            # t.daemon = True
            get_html_list.append(t)
            # all_list.append(t)
            t.start()
        # 等待子线程全部结束工作
        for i in get_html_list:
            i.join()

        # 创建解析线程
        for i in range(10):
            t = Thread(target=self.parse_page)
            parse_list.append(t)
            # all_list.append(t)
            t.start()
        # 一起关闭解析
        for i in parse_list:
            i.join()

        # 获取页面和解析一起进行,不推荐
        # for i in all_list:
        #     i.join()

    def put_url_to_queue(self):
        """添加url进入队列"""
        print(self.start, self.stop)
        for n in range(self.start, self.stop):
            params = {
                'page': n,
                'categoryId': self.type,
                'pageSize': '30'
            }
            url = self.base_url + urllib.parse.urlencode(params)
            self.url_queue.put(url)
        # print(self.url_queue.empty())

    def get_html_to_queue(self):
        """取出url获取页面，添加到解析队列"""
        while True:
            if self.url_queue.empty():
                print('url队列空了')
                break
            else:
                url = self.url_queue.get()
                res = requests.get(url, headers=self.headers)
                res.encoding = 'utf-8'
                html = res.text
                self.parse_queue.put(html)
                print("1")

    def parse_page(self):
        """解析页面"""
        while True:
            if self.parse_queue.empty():
                print('页面队列空了')
                break
            else:
                html = self.parse_queue.get()
                # 不推荐
                # try:
                #     html = self.parse_queue.get(block=True, timeout=2)
                #     app_info_list = json.loads(html)['data']
                #     for app_info in app_info_list:
                #         name = app_info['displayName']
                #         link = 'http://app.mi.com/details?id=' + app_info['packageName']
                #         d = {'应用名称': name, '下载链接': link}
                #         with open('xiaomi.json', 'a', encoding='utf8')as f:
                #             f.write(str(d) + '\n')
                # except Exception:
                #     break
                app_info_list = json.loads(html)['data']
                for app_info in app_info_list:
                    name = app_info['displayName']
                    link = 'http://app.mi.com/details?id=' + app_info['packageName']
                    d = {'应用名称': name, '下载链接': link}
                    with open('xiaomi.json', 'a', encoding='utf8')as f:
                        f.write(str(d) + '\n')
                print("2")


def test():
    begin = time.time()
    xiaomi = XiaoMiSpider()
    xiaomi.work_on()
    end = time.time()
    times = end - begin
    print("执行时间%.2f" % times)


if __name__ == '__main__':
    test()
