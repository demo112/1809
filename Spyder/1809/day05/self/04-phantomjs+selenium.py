import time
from selenium import webdriver


# 创建phantomjs对象
# driver = webdriver.PhantomJS(executable_path=)
driver = webdriver.PhantomJS()
driver.set_window_size(19200, 10800)
# 用个get方法发送请求,打开百度
driver.get('http://www.baidu.com')
# print(driver.page_source)
# 新增：接收重点输入的内容到搜索框
key = input('请输入要搜索的内容')
# 输入框
# id="kw"
kw = driver.find_element_by_id('kw')
kw.send_keys(key)
# 按钮
# id = "su"
su = driver.find_element_by_id('su')
su.click()
time.sleep(2)
# 获取屏幕截图
driver.save_screenshot('baidu.png')
# 关闭浏览器
driver.quit()
