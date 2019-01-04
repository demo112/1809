# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import nltk.corpus as nc
import nltk.classify as cf  # 分类器
import nltk.classify.util as cu

pdata = []  # 正面评论

fileids = nc.movie_reviews.fileids('pos')
print(fileids)
for fileid in fileids:
    words = nc.movie_reviews.words(fileid)

    sample = {}
    for word in words:
        sample[word] = True
    pdata.append((sample, 'POSITIVE'))

ndata = []  # 正面评论

fileids = nc.movie_reviews.fileids('neg')
for fileid in fileids:
    words = nc.movie_reviews.words(fileid)

    sample = {}
    for word in words:
        sample[word] = True
    ndata.append((sample, 'NEGATIVE'))

pnum, nnum = int(len(pdata) * 0.8), int(len(ndata) * 0.8)

train_data = pdata[:pnum] + ndata[:nnum]
test_data = pdata[pnum:] + ndata[nnum:]

#
model = cf.NaiveBayesClassifier.train(train_data)
ac = cu.accuracy(model, test_data)
print('%.2f%%' % round(ac * 100, 2))
# 影响最重要的特征
tops = model.most_informative_features()
for top in tops[:5]:
    print(top[0])

reviews = [
    'This is an amazing movie',
    'This is a dull movie.I would never recommend it to anyone',
    'The cinematography is pretty great ini this movie',
    'The direction was terrible and the story was all over place'
]

sents, probs = [], []
for review in reviews:
    words = review.split()
    sample = {}
    for word in words:
        sample[word] = True

    # 预测
    pcls = model.prob_classify(sample)
    sent = pcls.max()
    # 置信概率
    prob = pcls.prob(sent)
    sents.append(sent)
    probs.append(prob)

for review, sent, prob in zip(reviews, sents, probs):
    print(review, '->', sent, '%.2f%%' % round(prob * 100, 2))
