import requests
url = 'http://www.baidu.com/'
headers = {'User-agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)'}
# 发请求获取响应对象
res = requests.get(url, headers)
# 获取响应的编码格式,百度默认ISO-8859-1
print(res.encoding)
# 获取res的内容(字符串)
print(type(res.text))
# 指定内容编码
res.encoding = 'utf-8'
# 获取res的内容(bytes格式)
print(type(res.content))
# 获取HTTP响应码
print(res.status_code)
# 获取返回实际数据的URL地址
print(res.url)
