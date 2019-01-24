import urllib.request

url = 'http://www.baidu.com'
headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) '
                         'AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'}
req = urllib.request.Request(url, headers=headers)
res = urllib.request.urlopen(req)
html = res.read().decode('utf-8')
print(html)
