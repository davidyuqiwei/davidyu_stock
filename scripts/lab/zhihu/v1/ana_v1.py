import pandas as pd
from key_sents import *
df1 = pd.read_csv("./csv/answer_all.csv",header=None)
df1.columns=["title","similar_question","text"]

df2 = pd.read_csv("./circle_QA_may_ch.csv")

df3 = pd.concat([df1,df2],axis=1)

summarize = []
ans_text = df3.text.tolist()
for tt in ans_text:
    try:
        simi_text_summary = get_key_sents(tt,num=1)
        summarize.append(simi_text_summary)
    except:
        summarize.append("no")
df4=df3.assign(summarize_text=summarize)
df4.to_csv("zhihu_answers.csv",encoding="utf_8_sig")



