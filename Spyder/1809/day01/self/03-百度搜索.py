import urllib.request
import urllib.parse

# 定义常用变量
BASE_URL = 'http://www.baidu.com/s?'
KEY = input("请输入要搜索的内容：")
HEADERS = {'User-agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)'}

# 对url进行编码，拼接url
key = urllib.parse.urlencode({'wd': KEY})
url = BASE_URL + key
# 发送请求获取相应
req = urllib.request.Request(url, headers=HEADERS)
res = urllib.request.urlopen(req)
html = res.read().decode('utf-8')
# 保存到本地
with open('百度.html', 'w', encoding='utf-8') as f:
    f.write(html)
