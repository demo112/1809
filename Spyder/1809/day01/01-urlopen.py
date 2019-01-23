# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib.request
url = 'http://www.baidu.com/'
res = urllib.request.urlopen(url)
print(res.read().decode('utf-8'))