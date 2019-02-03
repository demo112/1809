# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
xpath_page = "//tr[@class='even'] | //tr[@class='odd']"
# 职位名称
work = "./td/a/text()"
# 类别
kind = "./td[2]/text()"
# 招聘人数
inneed = "./td[3]/text()"
# 招聘地点
position = "./td[4]/text()"
# 发布时间
time = "./td[5]/text()"
# 职位链接
link = "./td[1]/a/@href"
