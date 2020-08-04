from davidyu_cfg import *
from functions.stock_feature.mergeData import mergeData
data_file = "/home/davidyu/stock/data/test/day_history_kdj_macd_rsi_test.csv"

feature_list = ['kdjk','kdjd','kdjj','macdh',"rsi_6"]
df1 = pd.read_csv(data_file)
df_sample = df1.sample(frac=0.4)[feature_list+["slopes"]]


df_sample["slopes"] = mergeData.regPN(df_sample,'slopes')["slopes"]

df_sample.round(3).to_csv("/home/davidyu/stock/data/test/day_history_kdj_macd_rsi_sample.csv",index=0)



###########################################################################
###########################################################################


df2 = df1[df1["rsi_6"]>93]


a1 = df2.index.tolist() 

c = []  #生成一个空列表，用来放新列表
for i in range(len(a1)-1):
    b = a1[i+1] - a1[i] 
    if b != 1:
        c.append(a1[i])

df3 = df1.iloc[c,:]  

df3.slopes.max()
df3.slopes.min() 
df3.slopes.quantile(0.3)
df3.slopes.quantile(0.8)


index = []





