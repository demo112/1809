import time
from selenium import webdriver


# 创建phantomjs对象
# driver = webdriver.PhantomJS(executable_path=)
driver = webdriver.PhantomJS()

# 用个get方法发送请求
driver.get('http://www.youtube.com')
# print(driver.page_source)
# 获取屏幕截图
driver.save_screenshot('baidu.png')
# 关闭浏览器
driver.quit()
