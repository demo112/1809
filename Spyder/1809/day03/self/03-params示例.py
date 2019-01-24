import requests


key = input('key')
URL = 'http://www.baidu.com/s?'
HEADERS = {'User-agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)'}
params = {
    'wd': key,
    'pn': str(10)
}
res = requests.get(URL, headers=HEADERS, params=params)
res.encoding = 'utf-8'
html = res.text
print(html)
