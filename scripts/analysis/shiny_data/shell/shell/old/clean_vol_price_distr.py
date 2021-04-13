import pandas as pd
import sys
import gc
import os
#data_file = sys.argv[1] 
#df1 = pd.read_csv(data_file)

#df2 = df1[df1["price"]!="price"].drop_duplicates()
#df2.to_csv(data_file,index=0)


df1 = pd.read_csv("pv_dist_all.csv")
df2 = df1[df1["price"]!="price"].drop_duplicates()
#df2=df2.set_index("stock_index",drop=False)

#print(os.system("free -mh"))
del df1
gc.collect()
#print(os.system("free -mh"))
#stock_list = df2["stock_index"].unique().tolist()

stock_list = df2.groupby("stock_index").count().sort_values("dt",ascending=False).index.tolist()
df2=df2.set_index("stock_index",drop=False)
for i in stock_list:
    df3 = df2.loc[i]
    save_file = "../data/vol_prirce_distr/"+"pv_dist_"+i+".csv"
    df3.to_csv(save_file,index=0)
    df2 = df2.loc[~df2.index.isin([i])]
    gc.collect()
    #print(df2.shape)
    #print("##############"+i+"#############")
