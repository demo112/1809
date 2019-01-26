import hashlib
import random
import time
import navigator

key = 'tiger'
r = int(time.time() * 1000)
i = r + random.randint(0, 10)
sign = "fanyideskweb" + key + i + "p09@Bn{h02_BIEe]$P^nG"
s = hashlib.md5()
s.update(sign.encode())
sign_md5 = s.hexdigext()
# 根据版本号进行md5加密
bv = '7f2901ed530536104d65f4d3f630826a'
bv = key("./jquery-1.7").md5(navigator.appVersion)
