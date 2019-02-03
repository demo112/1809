from selenium import webdriver


class DouyuSpider(object):
    def __init__(self):
        self.base_url = 'https://www.douyu.com/directory/all'
        self.params = {

        }
        pass

    def work_on(self):

        self.get_page()
        pass

    def get_page(self):
        self.parse_page()
        pass

    def parse_page(self):
        pass