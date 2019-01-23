import csv
import re

html = '''
<div class="animal">
  <p class="name">
    <a title="Tiger"></a>
  <p>

  <p class="content">
    Two tigers two tigers run fast
  </p>
</div>

<div class="animal">
  <p class="name">
    <a title="Rabbit"></a>
  <p>

  <p class="content">
    Small white rabbit white and white
  </p>
</div>'''

p = re.compile('<div class="animal">.*?'
               'title="(\w+)".*?'
               '<p class="content">\s*(.*?)\s*</p>', re.S)
r = p.findall(html)
print(r)

for n in r:
    animal = n[0]
    content = n[1].strip()
    print(animal, '的', content)

# 将获取的数据存储到csv文件中
with open('animal.csv', 'w', newline='', encoding='gb18030') as f:
    writer = csv.writer(f)
    writer.writerow(r)
