from zhihu_v2 import *
import  pandas as pd
import time

df1 = pd.read_csv("circle_QA_may_ch.csv")
question = df1.title.tolist()


title = []
text = []
raw_title = []
k=1000
qu = question[k]
print(qu)
raw_title.append(qu)
title1,text1 = download_zhihu_ques_search(qu,1) 
title.append(title1[0])
text.append(text1[0])
os.system("pkill phantomjs")
#time.sleep(4)
df_list = {"raw_title":raw_title,
		"title": title,
		"text": text
	}
df = pd.DataFrame(df_list)
file_name = "./csv/answer_all.csv" 
df.to_csv(file_name,index=0, mode='a', header=False,encoding='utf_8_sig')
																		

