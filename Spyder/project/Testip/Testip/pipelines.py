# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
from threading import Thread

import requests
from multiprocessing import Queue

class TestipPipeline(object):
    def __init__(self):
        self.url = "http://httpbin.org/get"
        self.ip_queue = Queue()
        self.lines_list = []

    def process_item(self, item, spider):
        proxy = item['proxy'].split(' ')[0]
        print(proxy)
        # self.ip_queue.put(proxy)
        # self.check_ip()
        # for i in range(15):
        #     t = Thread(target=self.check_ip)
        #     self.lines_list.append(t)
        #     t.start()
        # for i in self.lines_list:
        #     i.join()
        return item

    def check_ip(self):
        while True:
            if self.ip_queue.empty():
                # print("队列处理完毕")
                break
            else:
                url = "http://httpbin.org/get"
                with open('proxy_list.csv', 'a', newline='', encoding='gb18030') as f:
                    writer = csv.writer(f)
                    proxy = str(self.ip_queue.get()).split(',')[0]
                    print(proxy)
                    proxies = {'http': 'http://' + proxy}
                    try:
                        res = requests.get(url, proxies=proxies, timeout=1)
                        if res.status_code == 200:
                        # if True:
                            writer.writerow(proxy)
                            print('yes', proxy)
                        else:
                            print(res.status_code)
                    except EnvironmentError:
                        # print('no', proxy)
                        pass
