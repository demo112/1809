import random
import urllib.request
import urllib.parse
from time import sleep


class BaiduSpyder(object):
    def __init__(self):
        self.BASE_URL = 'http://tieba.baidu.com/f?'
        self.TARGET = input("请输入目标贴吧")
        self.START = int(input("请输入起始页"))
        self.END = int(input("请输入结束页"))
        self.HEADERS_DIC = [
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

    # 获取页面
    def get_page(self, url):
        num = random.randint(0, len(self.HEADERS_DIC))
        headers = self.HEADERS_DIC[num]
        req = urllib.request.Request(url, headers=headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')
        print(num)
        return html

    # 解析页面
    def parse_page(self):
        pass

    # 保存数据
    @staticmethod
    def write_page(name='default', html=None):
        with open(name, 'w', encoding='utf-8') as f:
            f.write(html)
        pass

    # 主函数
    def work_on(self):
        for n in range(self.START, self.END + 1):
            sleep(0.2)
            key = urllib.parse.urlencode({'kw': self.TARGET})
            pn = (n - 1) * 50
            url = self.BASE_URL + key + '&' + urllib.parse.urlencode({'pn': pn})
            html = self.get_page(url)
            name = self.TARGET + str(n) + '.html'
            self.write_page(name=name, html=html)
            print(name)


if __name__ == '__main__':
    # 创建对象
    spider = BaiduSpyder()
    spider.work_on()
