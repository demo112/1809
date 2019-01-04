# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import warnings
warnings.filterwarnings(
    'ignore', category=UserWarning)
import nltk.tokenize as tk
import nltk.corpus as nc
import nltk.stem.snowball as sb
import gensim.models.ldamodel as gm
import gensim.corpora as gc


doc = []
with open('topic.txt') as f:
    for line in f.readlines():
        doc.append(line[:-1])


# 正则表达式分词器
tokenizer = tk.RegexpTokenizer(r'\w+')  # 使用1到多个空白字符分割

# 获取废词（出现频率高，但是语义贡献却很小的词）集合
stopwords = nc.stopwords.words('english')

# 创建思诺博词干提取器
stemmer = sb.SnowballStemmer('english')
lines_tokens = []
for line in doc:
    tokens = tokenizer.tokenize(line.lower())
    line_tokens = []
    for token in tokens:
        if token not in stopwords:
            token = stemmer.stem(token)
            line_tokens.append(token)
    lines_tokens.append(line_tokens)  # 变成二维列表
print(lines_tokens)

# 词典 升序排列
dic = gc.Dictionary(lines_tokens)

bow = []
for line_tokens in lines_tokens:
    row = dic.doc2bow(line_tokens)
    bow.append(row)

# 创建隐含狄利克雷分布
# passes=25 设置聚类的规模
model = gm.LdaModel(bow, num_topics=2, id2word=dic, passes=25)
# 类似聚类的方法 提取文档中的主题词
topics = model.print_topics(num_topics=2, num_words=4)
print(topics)
