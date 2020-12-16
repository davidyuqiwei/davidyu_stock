from davidyu_cfg import *
import pandas as pd
from functions.baostock.stock_slope import *

df1 = pd.read_csv("huigou_out_data.csv")

df_out = pd.DataFrame()
stat_days = 1
pred_days = 30
out_slope = []
pred_days_list = [5,10,15,20,30,60,90]
out_slope = []
out_slope_name = []
for pred_days in pred_days_list:
    slope_name = "slope_"+str(pred_days)
    out_slope_name.append(slope_name)

for i in range(0,df1.shape[0]):
    for pred_days in pred_days_list:
        stock_index = str(df1["stock_index"][i]).zfill(6)
        start_date = df1["stock_date"][i]
        slope,pred_start_date,pred_end_date = stockSlope(stock_index,start_date,stat_days,pred_days)
        #print(slope)
        out_slope.append(slope)
    insert_data = [stock_index,start_date,pred_start_date,pred_end_date]+out_slope
    out_slope = []
    if -999 in insert_data:
        pass
    else:
        df_out=df_out.append(pd.DataFrame(insert_data).T)

df_out.columns = ["stock_index","start_date","pred_start_date","pred_end_date"]+out_slope_name
df_out.to_csv("huigou_slope.csv",index=0)

