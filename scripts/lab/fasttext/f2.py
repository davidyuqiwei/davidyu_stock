# _*_ coding:utf-8 _*_

'''
@Author: Ruan Yang
@Date: 2018.12.9
@Purpose: 处理wikizh文本的二分类问题，判断语句是否通顺
@Attention: 本例中的负样本是 shuffle 正样例得到，所以容易形成分类
@算法：CNN
@本例是二分类问题
'''

import codecs

paths=r"/home/davidyu/gits/fastText-Study/"

train_data_name="train.txt"
test_data_name="test.txt"

x_train=[]
x_test=[]
y_train=[]
y_test=[]

x_train_positive=0
x_train_negative=0
x_test_positive=0
x_test_negative=0

with codecs.open(paths+train_data_name,"r","utf-8") as f1,\
     codecs.open(paths+test_data_name,"r","utf-8") as f2:
    for line in f1:
        words=line.strip().split("\t")
        if words[0] == "__label__1":
            y_train.append([0,1]) # [0,1] 表示正样例
            x_train_positive += 1
        else:
            y_train.append([1,0]) # [1,0] 表示负样例
            x_train_negative += 1
        x_train.append(words[1])
        
    for line in f2:
        words=line.strip().split("\t")
        if words[0] == "__label__1":
            y_test.append([0,1])
            x_test_positive += 1
        else:
            y_test.append([1,0])
            x_test_negative += 1
        x_test.append(words[1])
        
print("#----------------------------------------------------------#")
print("训练集总数：{}".format(len(x_train)))
print("训练集中正样本个数：{}".format(x_train_positive))
print("训练集中负样本个数：{}".format(x_train_negative))
print("测试集总数：{}".format(len(x_test)))
print("测试集中正样本个数：{}".format(x_test_positive))
print("测试集中负样本个数：{}".format(x_test_negative))
print("#----------------------------------------------------------#")
print("\n")

print("#----------------------------------------------------------#")
print("将输入文本转换成 index - word 对应关系，并输出词汇表")
x_text=x_train+x_test # 总输入文本
y_labels=y_train+y_test


x_text=x_train+x_test # 总输入文本
y_labels=y_train+y_test


from tensorflow.contrib import learn
import tensorflow as tf
import numpy as np
import collections


max_document_length=200
min_frequency=1


vocab = learn.preprocessing.VocabularyProcessor(max_document_length,min_frequency, tokenizer_fn=list)

str1="""工行17年全年实现营收7265亿元,同比增7.5%,较16年负增3.12%成功实现筑底回升,Q1-Q4单季盈利同比增速分别为19.86%、-8.92%、0.58%、9.85%,增长趋势较为明确。得益于营
业成本压降3.58%,PPOP和归母净利润分别增长9.12%/2.80%,较16年增速分别提升8.97/2.40个百分点。拆分来看,非息收入同比收降9.57%,其中手续费收入降幅3.69%,主要是受个人理
财手续费下降12.7%影响。因而盈利的增厚主要来自于利息收入。公司全年利息净收入5,220.78亿元,同比增长10.6%,占总营收的77.3%(+3.74pct,YoY)。我们认为净利息收入的增长>一方面来源于生息资产规模的稳健提升,另一方面源于净息差的企稳走阔。工行17年实现净
息差2.22%,同比16年增厚6BP,单季度数据逐步上行"""
list(vocab.fit_transform(["稳步增长"])) 
list(vocab.fit_transform([str1])) 

x = np.array(list(vocab.fit_transform(x_text)))
vocab_dict = collections.OrderedDict(vocab.vocabulary_._mapping)







