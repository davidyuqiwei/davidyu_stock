import pandas as pd
import os
from davidyu_cfg import *
#data_path = '/home/davidyu/stock/data'
def dfcf_stock_data(stock_index,start_date="1900-01-01",end_date="2050-01-01"):
    df_dir = os.path.join(data_path,"history_data","dfcf_fuquan","stock_index")
    df1 = pd.read_csv(os.path.join(df_dir,stock_index+"_fuquan.csv"))
    df1 = df1[(df1["dt"]>=start_date)&(df1["dt"]<=end_date)]
    df1 = df1.drop_duplicates()
    df1 = df1.sort_values("dt")
    df1["stock_index"] = [ str(x).zfill(6) for x in df1["stock_index"]]
    return df1

