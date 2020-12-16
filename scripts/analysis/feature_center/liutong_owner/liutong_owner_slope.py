from davidyu_cfg import *
import pandas as pd
from functions.baostock.stock_slope import *
df1 = pd.read_csv("liutong_data.csv",header=None)
df1.columns = ["owner_rank","owner","vol","ratio","type","stock_date","stock_index"]
stat_days = 60
pred_days = 30
df_out = pd.DataFrame()
pred_days_list = [5,10,15,20,30]
#for i in range(0,df1.shape[0]):
out_slope = []
out_slope_name = []
for pred_days in pred_days_list:
    slope_name = "slope_"+str(pred_days)
    out_slope_name.append(slope_name)
#for i in range(0,10):
for i in range(0,df1.shape[0]):
    for pred_days in pred_days_list:
        stock_index = str(df1["stock_index"][i]).zfill(6)
        start_date = df1["stock_date"][i]
        vol = df1["vol"][i]
        ratio = df1["ratio"][i]
        slope,pred_start_date,pred_end_date = stockSlope(stock_index,start_date,stat_days,pred_days)
        out_slope.append(slope)
    insert_data = [stock_index,start_date,vol,ratio,pred_start_date,pred_end_date]+out_slope
    out_slope = []
    if -999 in insert_data:
        pass
    else:
        df_out=df_out.append(pd.DataFrame(insert_data).T)


#print(df_out)
df_out.columns = ["stock_index","start_date","val","ratio","pred_start_date","pred_end_date"]+out_slope_name
#print(df_out)
df_out.to_csv("liutong_owner_slope.csv",index=0)
