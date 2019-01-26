import os
import re
import time

import requests
from user_agent import UserAgent


# noinspection PyTypeChecker
class GetNote(object):
    def __init__(self):
        self.user_agent = UserAgent()
        self.base_url = 'http://code.tarena.com.cn/'
        self.params = {}
        self.proxies = {"http": "http://" + self.user_agent.choice_ip()}
        self.headers = self.user_agent.choice_headers()
        self.auth = ('tarenacode', 'code_2018')
        # self.path = '/Users/cooper/Library/Mobile\ Documents/com~apple~CloudDocs/AID/cooper_Python'
        self.path = '/Users/cooper/Library/Mobile Documents/com~apple~CloudDocs/AID/cooper_Python/Note'
        self.html = ''
        self.url = ''

    def get_page(self, url):
        # 打开页面，并获取
        self.url = url
        res = requests.get(
            url=url,
            params=self.params,
            headers=self.headers,
            auth=self.auth)
        res.encoding = 'utf-8'
        # time.sleep(0.3)
        html = res.text
        self.parse_page(html)

    def parse_page(self, html):
        # 解析页面
        p = re.compile('<a href="(.*?)">.*?\.?.*?</a>', re.S)
        file_list = p.findall(html)
        print(file_list)
        self.write_page(file_list)

    def write_page(self, ls):
        # print(self.url)
        with open('Note.txt', 'a') as f:
            back_url = self.url
            for ur in ls:
                # time.sleep(1)

                if ur == ('../' or './'):
                    pass
                else:
                    # print(ur)
                    # f.write(ur + '\n')
                    name = ur.split('.')
                    # 区分路径和文件
                    if len(name) >= 2:
                        # this is a file
                        self.url += ur
                        # print(self.url)
                        f.write(self.url + '\n')
                        self.download_file(self.url, ur)
                        self.url = back_url
                    else:
                        self.url += ur
                        # print(self.url)
                        # print(ur)
                        self.get_page(self.url)
                        self.url = back_url
                        # this is a package

    def download_file(self, url, file):
        header = self.user_agent.choice_headers()
        res = requests.get(url, headers=header, auth=self.auth)
        res.encoding = 'utf-8'
        html = res.content
        file_path = self.set_path(file)
        # todo 判断文件是否存在
        print(file_path)
        try:
            with open(file_path, 'wb') as f:
                f.write(html)
        except Exception:
            print("该文件未下载", file_path)

    def work_on(self):
        self.get_page(self.base_url)

    def get_path(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # print(BASE_DIR)
        return BASE_DIR

    def set_path(self, file):
        self.path_url_part = '/'.join(self.url.split('/')[3:][:-1])
        print(self.path_url_part)
        self.mkdir(self.path + '/' + self.path_url_part)
        file_path = self.path + '/' + self.path_url_part + '/' + file
        return file_path

    def mkdir(self, path_part):
        folder = os.path.exists(path_part)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(path_part)  # makedirs 创建文件时如果路径不存在会创建这个路径
            # print("---  new folder...  ---")
            # print("---  OK  ---")
            return path_part
        else:
            pass
            # print("---  There is this folder!  ---")


if __name__ == '__main__':
    spider = GetNote()
    # spider.work_on()
    url = 'http://code.tarena.com.cn/AIDCode/aid1807/AID1807/HTTPServer/WebFrame/static/http://http://www.python.org'
    spider.parse_page(url)