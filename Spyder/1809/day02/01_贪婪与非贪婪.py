import re

html = """
<div><p>苟利国家生死以</p></div>
<div><p>床前明月光</p></div>
"""

# 贪婪匹配
p = re.compile('<div><p>.*</p></div>', re.S)            # 创建编译对象
r = p.findall(html)
print(r)

# 非贪婪匹配
re_compile = re.compile('<div><p>.*?</p></div>', re.S)  # 创建编译对象
p = re_compile
r = p.findall(html)
print(r)

p = re.compile('<div><p>[\s\S]*?</p></div>')
rlist = p.findall(html)
print(rlist)
