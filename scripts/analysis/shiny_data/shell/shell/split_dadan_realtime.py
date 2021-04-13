import pandas as pd
import sys
import gc
import os
from davidyu_cfg import *

from functions.common.TimeMake import *



df1 = pd.read_csv("../data/dadan_realtime_daily_max.csv")
df2 = pd.read_csv("../data/dadan_realtime_daily_max_sell.csv")
df_raw3 =  pd.read_csv("../data/dadan_realtime_daily_sum.csv")

days = timeFunc.getEveryDay(min(df1["dt"].min(),df2["dt"].min()),max(df1["dt"].max(),df2["dt"].max()))
df_days = pd.DataFrame(days)
df_days.columns = ["dt"]

stock_list = df1["stock_index"].unique().tolist() 
for i in stock_list:
    df3 = df1[df1["stock_index"]==i]
    df3 = pd.merge(df_days,df3, how='left')
    df4 = df2[df2["stock_index"]==i]
    df4 = pd.merge(df_days,df4, how='left')
    df5 = df_raw3[df_raw3["stock_index"]==i]
    df5 = pd.merge(df_days,df5, how='left')
    save_file = "../data/dadan_realtime/"+"dadan_realtime_"+str(i).zfill(6)+".csv"
    sell_save_file = "../data/dadan_realtime/"+"dadan_realtime_sell_"+str(i).zfill(6)+".csv"
    save_file_daily_sum = "../data/dadan_realtime/"+"dadan_realtime_daily_sum_"+str(i).zfill(6)+".csv"
    df3.sort_values("dt").to_csv(save_file,index=0)
    df4.sort_values("dt").to_csv(sell_save_file,index=0)
    df5.sort_values("dt").to_csv(save_file_daily_sum,index=0)
