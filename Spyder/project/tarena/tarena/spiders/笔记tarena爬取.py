import os
import re
import time

import requests
import requests.adapters
from Spyder.project.tarena.tarena.spiders.user_agent import UserAgent



# noinspection PyTypeChecker
class GetNote(object):
    def __init__(self):
        self.user_agent = UserAgent()
        self.proxies = {"http": "http://" + self.user_agent.choice_ip()}
        # self.proxies = {"http": "http://127.0.0.1"}
        self.headers = self.user_agent.choice_headers()
        self.auth = ('tarenacode', 'code_2018')
        # self.path = '/Users/cooper/Library/Mobile\ Documents/com~apple~CloudDocs/AID/cooper_Python'
        self.path = '/Users/cooper/Library/Mobile Documents/com~apple~CloudDocs/AID/cooper_Python/Note'
        self.html = ''
        self.url = ''

    def work_on(self, url):
        time.sleep(0.01)
        requests.adapters.DEFAULT_RETRIES = 5
        s = requests.session()
        s.keep_alive = False
        # print('开始链接')
        with open("Note.txt", 'a') as f:
            # print('日志打开')
            html = self.get_page(url)
            file_list = self.parse_page(html)
            # with open('Note.txt', 'a') as f:
            back_url = self.url
            for ur in file_list:
                if ur == ('../' or './'):
                    pass
                else:
                    # print(ur)
                    # f.write(ur + '\n')
                    name = ur.split('.')
                    # 区分路径和文件
                    if len(name) >= 2 or name[-1] == 'html':
                        # this is a file
                        if self.check_history():
                            print('日志已存在', self.url)
                            continue
                        if self.check_file(ur):
                            f.write(self.url + '\n')
                            print('文件已下载', self.url)
                            continue
                        self.write_page(ur, f, back_url)
                    else:
                        # this is a package
                        self.url += ur
                        # print(self.url)
                        # print(ur)
                        self.work_on(self.url)
                        self.url = back_url

    def get_page(self, url):
        # 打开页面，并获取，更改全局当前url状态
        self.url = url
        res = requests.get(
            url=url,
            headers=self.headers,
            auth=self.auth)
        res.encoding = 'utf-8'
        # time.sleep(0.3)
        html = res.text
        # print(html)
        return html

    def parse_page(self, html):
        # 解析页面，查找出所有链接（文件或下一级网页）
        p = re.compile('<a href="(.*?)">.*?\.?.*?</a>', re.S)
        file_list = p.findall(html)
        # print(file_list)
        return file_list

    def write_page(self, ur, f, back_url):
        self.url += ur  + '\n'
        # print(self.url)
        f.write(self.url)
        self.download_file(self.url, ur)
        self.url = back_url

    def download_file(self, url, file):
        file_path = self.set_path(file)
        header = self.user_agent.choice_headers()
        res = requests.get(url, headers=header, auth=self.auth)
        res.encoding = 'utf-8'
        data = res.content
        print('下载中：', file_path)
        try:
            with open(file_path, 'wb') as f:
                f.write(data)
        except Exception as e:
            print("该文件未下载", file_path, e)

    def get_path(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # print(BASE_DIR)
        return BASE_DIR

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

    def check_history(self):
        # 检测url是否已存在于已下载列表内
        flag = False
        with open('Note.txt', 'r') as f:
            for line in f.readlines():
                if self.url == line.strip():
                    # print(self.url)
                    # print(line)
                    # print('存在下载日志')
                    flag = True
            # print(flag)
        return flag

    def set_path(self, file):
        # 将路径中文件树部分与本地根目录路径拼接后创建文件夹
        # 并追加文件名称生成文件本地路径
        self.path_url_part = '/'.join(self.url.split('/')[3:][:-1])
        # print(self.path_url_part)
        self.mkdir(self.path + '/' + self.path_url_part)
        file_path = self.path + '/' + self.path_url_part + '/' + file
        return file_path

    def check_file(self, file):
        flag = False
        file_path = self.set_path(file)
        # 判断文件是否存在
        if os.access(file_path, os.F_OK):
            # print('文件已经存在')
            flag = True
        return flag


if __name__ == '__main__':
    base_url = 'http://code.tarena.com.cn/'
    spider = GetNote()
    spider.work_on(base_url)
    # url = 'http://code.tarena.com.cn/AIDCode/aid1807/AID1807/HTTPServer/WebFrame/static/http://http://www.python.org'
    # spider.parse_page(url)
