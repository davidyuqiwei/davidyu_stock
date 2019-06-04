from key_sents import *
import pandas as pd
df1 = pd.read_csv("QA_zhihu_1.csv")

tt1=df1.text.tolist()[3]

ks = get_key_sents(tt1,num=1)

print(ks)


