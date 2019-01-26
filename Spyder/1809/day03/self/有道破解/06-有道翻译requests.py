import string
import urllib.request
import urllib.parse
import json
import hashlib
import random
import time

# 接收用户输入
key = input("请输入要翻译的内容:")
ts = int(time.time() * 1000)
salt = ts + random.randint(0, 10)
sign = "fanyideskweb" + key + str(salt) + "p09@Bn{h02_BIEe]$P^nG"
s = hashlib.md5()
s.update(sign.encode())
sign_md5 = s.hexdigest()
# 根据版本号进行md5加密
bv = '7f2901ed530536104d65f4d3f630826a'
# 把Form Data定义成1个大字典
data = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": str(salt // 10),
        "sign": sign_md5,
        "ts": ts,
        "bv": '7f2901ed530536104d65f4d3f630826a',
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }
# 把data转为bytes数据类型
data = urllib.parse.urlencode(data).encode("utf-8")
# 发请求,获响应,获取内容
# 此处的URL地址为F12抓到的POST的地址,去掉translate_o中的 "_o"
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '256',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=1449841678.9953127; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; OUTFOX_SEARCH_USER_ID=1291895414@113.128.229.62; JSESSIONID=abck00ZXS24Lc_tNQg-Hw; ___rl__test__cookies=1548323032899',
        'DNT': '1',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        }
req = urllib.request.Request(url, data=data, headers=headers)
print(111)
res = urllib.request.urlopen(req)
print(111)
html = res.read().decode("utf-8")
print(html)
# 把json格式的字符串转为python中字典
rDict = json.loads(html)
result = rDict["translateResult"][0][0]["tgt"]
print(result)


# {'type': 'EN2ZH_CN',
# 'errorCode': 0, 
# 'elapsedTime': 1, 
# 'translateResult': 
#     [[{'src': 'tiger', 'tgt': '老虎'}]]}

# print(string.__all__)
