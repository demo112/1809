import csv
import time
import requests
from multiprocessing import Queue
from threading import Thread
from user_agent import UserAgent


class CheckIpManyline(object):
    def __init__(self):
        self.user_agent = UserAgent()
        self.headers = self.user_agent.choice_headers()
        self.url = "http://httpbin.org/get"
        self.ip_queue = Queue()
        self.lines_list = []

    def work_on(self):
        self.inline()
        for i in range(100):
            t = Thread(target=self.check_ip)
            self.lines_list.append(t)
            t.start()
        for i in self.lines_list:
            i.join()

    def inline(self):
        list_len = self.user_agent.ip_lens()
        for n in range(list_len):
            ip = self.user_agent.check_ip(n)
            self.ip_queue.put(ip)

    def check_ip(self):
        while True:
            if self.ip_queue.empty():
                print("队列处理完毕")
                time.sleep(0.1)
                break
            else:
                with open('ip_sea.csv', 'w', newline='') as f:
                    writer = csv.writer(f)
                    ip = self.ip_queue.get()
                    proxy = {'http': 'http://' + ip}
                    try:
                        res = requests.get(self.url, proxies=proxy, headers=self.headers, timeout=3)
                        if res.status_code == 200:
                            # ip_sea.append(ip)
                            ip, port = ip.split(':')
                            writer.writerow('%s' % ip)
                        print('yes', ip)
                    except EnvironmentError:
                        print('no', ip)


if __name__ == "__main__":
    begin = time.time()
    ipsea = CheckIpManyline()
    ipsea.work_on()
