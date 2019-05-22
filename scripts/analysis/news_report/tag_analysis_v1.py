from collections import defaultdict
import os
import re
import jieba
import codecs
from nltk.probability import  FreqDist,ConditionalFreqDist
import jieba.analyse
from tqdm import tqdm
import pandas as pd
dict_david=jieba.load_userdict("/home/davidyu/software/Anaconda/lib/python3.7/site-packages/jieba/dict_davidyu.txt")


file_in="/home/davidyu/stock/data/news_report/600728/600728_2017-11-09_31.txt"

def get_label(file_in):
    ttt=open(file_in)
    t2=ttt.readlines()
    t4=[x.rstrip("\n") for x in t2]
    article=[]
    t3="".join(t4).replace(" ","") 
    #keywords = jieba.analyse.extract_tags(t3, topK=20, withWeight=True, allowPOS=('n','nr','ns'))
    keywords = jieba.analyse.extract_tags(t3, topK=20, withWeight=False)
    if '增长' in keywords:
        lab = '__label__1'
    else:
        lab = '__label__0'
    return lab,t3

#lab1,texts=get_label(file_in)

path1="/home/davidyu/stock/data/news_report/"
#for i in os.walk(path1):
#    print(i)
label_all=[]
text_all=[]
print("total loop is   "+str(len(list(os.walk(path1)))))
for pathe,dirs,fs in tqdm(os.walk(path1)):
    for f in fs:
        #print(os.path.join(fpathe,f))
        try:
            file_in=os.path.join(pathe,f)
            lab1,texts=get_label(file_in)
            label_all.append(lab1)
            text_all.append(texts)
        except:
            pass

df_text={
        "label": label_all,
        "text": text_all
        }

df_all=pd.DataFrame(df_text)
df_all.groupby("label").count()


valid_v1=random.sample(range(0,df_all.shape[0]),5000)
train_v1=list(set(range(0,df_all.shape[0])) ^ set(select_v1))

df_valid=df_all.loc[valid_v1,:]
df_train=df_all.loc[train_v1,:]

df_valid.to_csv("valid_text.txt",index=0,header=None,sep="\t")
df_train.to_csv("train_text.txt",index=0,header=None,sep="\t")




def test_fasttext():
	import os
	import codecs
	from fastText import train_supervised
	
	
	data_dir="/home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/news_report"
	train_data = os.path.join(data_dir,"train_text.txt")
	valid_data=os.path.join(data_dir,"valid_text.txt")
	
	model = train_supervised(input=train_data, epoch=50, lr=0.5, wordNgrams=2, dim=100,verbose=2, minCount=1,thread=1)
	model = train_supervised(input=train_data, epoch=50, lr=0.5, wordNgrams=2, dim=100,verbose=2, minCount=1,thread=1,loss="softmax")
	
	print_results(*model.test(valid_data))

pre_str=pd.read_csv("valid_text.txt",sep="\t",header=None) 
strings=pre_str.loc[:,1].tolist()
label_valid=pre_str.loc[:,0].tolist()
pred_label=[]
for string in strings:
    result=model.predict(string)
    pred_label.append(result[0][0])



string1="""事件:近日,佳都科技发布2018年三季度报告,前三季度公司实现营业收入27.90亿元,同比增长17.29%;实现归属母公司股东净利润1.13亿元,同比增长
110.43%。基本每股收益0.0702元,同比增长108.93%。   点评:   业绩稳健提升,净利润保持快速增长。三季度公司业绩维持较快增长,其中营收同比增速为12.86%,相较上半年有所回落,归母净利润同比增速达到115.64%,与上半年增速相比小幅提升。与半年报情况类似,利润的快速增长依旧主要是得益于销售毛利率的提升>以及费用的有效管控。三季度公司的销售毛利率及净利率分别为14.05%和4.07%,较上年同期分别明显提升了2.42和1.97个百分点,再次印证了公司今年以来盈利能
力的提升。前三季度期间费用率为7.95%,较上半年度下降2.55个百分点,下降幅度明显。其中,主要是管理费用和销售费用得到管控所致。   研发投入高增长,助>力产品智能化升级。公司重视技术研发,前三季度公司累计研发投入达到7079.35万元,同比增长54.36%,远高于公司营收增速。持续的研发投入有助于实现公司产>品的智能化升级和附加值的提升。近期,公司参股公司云从科技完成B+轮融资,金额总计超过10亿元人民币。云从科技是国内计算机视觉领域的领先企业,业务方向
侧重于金融和安防,已经成为中国银行业主要AI供应商。"""

result=model.predict(string1)


'''


import time
k=0
for i in tqdm(os.walk(path1)):
    time.sleep(0.001)
    k+=1

'''      



