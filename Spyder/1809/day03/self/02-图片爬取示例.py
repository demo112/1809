import requests

URL = 'http://image.baidu.com/search/detail?ct=503316480&z=9&tn=baiduimagedetail&ipn=d&word=%E8%B5%B5%E4%B8%BD%E9%A2%96&step_word=&ie=utf-8&in=&cl=2&lm=-1&st=-1&hd=undefined&latest=undefined&copyright=undefined&cs=3504584297,2344858995&os=2380293071,672998532&pn=0&rn=1&di=50160333440&ln=3864&fr=&fmq=1548295372062_R_D&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=&height=&face=undefined&is=0,0&istype=2&ist=&jit=&bdtype=11&pi=0&gsm=0&objurl=http%3A%2F%2Fdingyue.nosdn.127.net%2F4gmfZm9tBWMGUAfkpqSkiSmlfFZdoPYojSYJzT3MDXtfN1547928783087compressflag.jpeg&rpstart=0&rpnum=0&adpicid=0'
HEADERS = {'User-agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)'}

# 发请求
res = requests.get(URL, headers=HEADERS)
# 获取bytes响应内容
html = res.content

with open("zhaoliying.jpeg", 'wb') as f:
    f.write(html)
    print("图片下载成功")
