from selenium import webdriver

# driver = webdriver.PhantomJS()
opt = webdriver.ChromeOptions()
opt.set_headless()
# todo chromedriver版本不支持
driver = webdriver.Chrome(options=opt)

driver.get('http://www.qiushibaike.com/text/')
kw = driver.find_element_by_class_name('content')
kw_list = driver.find_elements_by_class_name('content')
print(kw.text)
print(kw.tag_name)
for kw in kw_list:
    print(kw.text)
