import time
import requests
from lxml import etree
from user_agent import UserAgent

# 分析贴吧主页
# http://tieba.baidu.com/f?
# http://tieba.baidu.com/f?kw=%E6%A0%A1%E8%8A%B1&ie=utf-8&pn=50
# 提取所有帖子中的url
user_agent = UserAgent()


class BaiduTieba(object):
    """
        思路：
        使用xpath
        1，先考虑获取下一页的链接规律
        2。将每一页所有帖子的链接
        3。获取帖子内的下一页链接规律
        4。将每一页中的图片保存
    """
    def __init__(self):
        self.base_url = 'http://tieba.baidu.com/f?'
        self.headers = user_agent.choice_headers()
        self.ip = user_agent.choice_ip()
        self.proxies = {"http": "http://" + self.ip}

    def work_on(self):
        target = input("请输入")
        start = int(input('start'))
        # start = 1
        stop = int(input('stop'))
        # stop = 1
        for n in range(start, stop + 1):
            pn = (n - 1) * 50
            params = {
                'kw': target,
                'pn': pn,
            }
            self.get_page(params)

    def get_page(self, params):
        """获取列表"""
        res = requests.get(self.base_url,
                           headers=self.headers,
                           # proxies=self.proxies,
                           params=params)
        res.encoding = 'utf-8'
        html = res.text
        self.parse_page(html)

    def parse_page(self, html):
        # print(1)
        # 解析网页，获取帖子链接列表
        xpath = "//div[@class='t_con cleafix']/div/div/div/a/@href"
        parse_html = etree.HTML(html)
        topic_list = parse_html.xpath(xpath)
        print(topic_list)
        for topic in topic_list:
            topic_link = 'http://tieba.baidu.com' + topic
            self.get_img(topic_link)

    def get_img(self, link):
        # print(5)
        # 请求链接，获取帖子网页
        # print(link)
        res = requests.get(link,
                           # proxies=self.proxies,
                           headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text

        # with open('hahahahhaha.html', 'w') as f:
        #     f.write(html)
        self.save_file(html)
        pass

    def save_file(self, img_html):
        # print(2)
        # 解析网页获取图片地址列表
        # print(img_html)
        # xpath = '//div[@class="video_src_wrapper"]/div/video/@src'
        # xpath = '//cc/div/img[@class="BDE_Image"]/@src | //div[@class="video_src_wrapper"]/embed/@data-video'
        xpath = '//div[@class="video_src_wrapper"]/embed/@data-video'
        parse_img = etree.HTML(img_html)
        img_list = parse_img.xpath(xpath)
        # print(img_list)
        self.write_img(img_list)

    def write_img(self, img_list):
        print(img_list)
        for img in img_list:
            filename = img[-10:]
            res = requests.get(img, headers=self.headers)
            res.encoding = 'utf-8'
            img = res.content
            with open(filename, 'wb') as f:
                f.write(img)
                print("下载成功", img)
                time.sleep(1)


if __name__ == '__main__':
    tieba = BaiduTieba()
    tieba.work_on()
# //cc/div[@id='post_content_123805678675']/img[@class='BDE_Image'][*]/@src
# //cc/div[@id='post_content_123805678675']/img[@class='BDE_Image'][2]/@src
# http://tieba.baidu.com/p/6017523439
# http://tieba.baidu.com/f?kw=%E6%A0%A1%E8%8A%B1&ie=utf-8
