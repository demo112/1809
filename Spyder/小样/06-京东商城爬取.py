from selenium import webdriver
import time
import csv


opt = webdriver.ChromeOptions()
opt.set_headless()
driver = webdriver.Chrome(options=opt)

driver.get('https://www.jd.com/')
key = input("请输入搜索内容")
driver.find_element_by_id('key').send_keys(key)
driver.find_element_by_class_name('button').click()
time.sleep(2)
page = 0
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    # 每一页中的商品信息列表读取
    xpath_goods = "//div[@class='ml-wrap']/div[@id='J_goodsList']/ul[@class='gl-warp clearfix']/li"
    goods_list = driver.find_elements_by_xpath(xpath_goods)
    with open('books.csv', 'a', newline='', encoding='gb18030') as f:
        writer = csv.writer(f)
        # writer.writerow(["价格", "名称", "评价", "书店"])
        for goods in goods_list:
            info_list = goods.text.split('\n')
            if '拍拍' in info_list:
                info_list.remove('拍拍')
            # print(info_list)
            # 每一个商品信息提取
            price = info_list[0]
            name = info_list[1]
            commit = info_list[2]
            market = info_list[3]
            info_ls = [price, name, commit, market]
            writer.writerow(info_ls)
    next_page = driver.page_source.find('pn-next disable')
    if next_page == -1:
        page += 1
        print("第%d页爬取成功" % page)
        driver.refresh()
        driver.find_element_by_class_name('pn-next').click()
        time.sleep(1.3)
    else:
        break
driver.quit()
