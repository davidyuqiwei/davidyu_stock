from collections import defaultdict
import os
import re
import jieba
import codecs
from nltk.probability import  FreqDist,ConditionalFreqDist

dict_david=jieba.load_userdict("/home/davidyu/software/Anaconda/lib/python3.7/site-packages/jieba/dict_davidyu.txt")
<<<<<<< HEAD
ttt=open("/home/davidyu/stock/data/news_report/600728/600728_2017-11-09_31.txt")
=======
ttt=open("/home/davidyu/stock/data/news_report/600728_2017-11-09_31.txt")
>>>>>>> 1f748b377819d67350ada8ca8130fda7752e2a91
t2=ttt.readlines()
t4=[x.rstrip("\n") for x in t2]
article=[]
t3="".join(t4).replace(" ","") 

segList = jieba.cut(t3,cut_all = True)
segResult=[]

f1=open("/home/davidyu/gits/stopwords/百度停用词表.txt")
f_txt=f1.readlines()
stopwords=[x.split("\n")[0] for x in f_txt]

for word in segList:
    if word in stopwords or word == '':
        continue
    else:
        segResult.append(word)

dict([(word,True) for word in segResult])


word_fd = FreqDist()
cond_word_fd = ConditionalFreqDist()
for word in segResult:
    word_fd[word] += 1
    cond_word_fd['pos'][word] += 1
from nltk.metrics import  BigramAssocMeasures

total_word_count = pos_word_count + 100
for word, freq in word_fd.items():
    pos_score = BigramAssocMeasures.chi_sq(cond_word_fd['pos'][word], 
            (freq, pos_word_count), total_word_count)

for word, freq in word_fd.items():
    print(word)
    print(freq)

from snownlp import SnowNLP
text=u"股市会上涨."
s = SnowNLP(text)
s2 = SnowNLP(s.sentences)
s2.sentiments 





'''
segList = jieba.cut(sentence)
segResult = []
    for w in segList:
    segResult.append(w)

'''





