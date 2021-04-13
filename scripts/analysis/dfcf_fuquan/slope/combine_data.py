import pandas as pd
from davidyu_cfg import *


df1 = pd.read_csv("dazongjiaoyi_select_data.csv")
df2 = pd.read_csv("slope_out.txt",header=None)
df2.columns = ["stock_index","start_date","end_date","days_num","slope"]
df_m1 = pd.merge(df1,df2,on=["stock_index"], how='left')
print(df_m1.head(10))

