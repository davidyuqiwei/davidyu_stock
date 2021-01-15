import pandas as pd
import os
from davidyu_cfg import *
data_path = '/home/davidyu/stock/data'
def stock_data(stock_index,start_date,end_date):
    df_dir = os.path.join(data_path,"history_data","baostock","2020-12-17")
    df1 = pd.read_csv(os.path.join(df_dir,stock_index+".csv"))
    df1 = df1[(df1["dt"]>=start_date)&(df1["dt"]<=end_date)]
    df1 = df1.drop_duplicates()
    df1 = df1.sort_values("date")
    df1["stock_index"] = [ x[3:9] for x in df1["code"]]
    return df1

