from davidyu_cfg import *
import pandas as pd
from functions.baostock.stock_slope import *
df1 = pd.read_csv("hk_increase.csv",header=None)
df1.columns = ["stock_index","stock_name","industry","ratio_change","a_ratio","b_ratio",
    "end_date","start_date","owner_name"]
stat_days = 28
pred_days = 30
df_out = pd.DataFrame()
pred_days_list = [5,10,15,20,30,60,90]
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
        start_date = df1["end_date"][i]
        a_ratio = df1["a_ratio"][i]
        b_ratio = df1["b_ratio"][i]
        ratio_change = df1["ratio_change"][i]
        slope,pred_start_date,pred_end_date = stockSlope(stock_index,start_date,stat_days,pred_days)
        out_slope.append(slope)
    insert_data = [stock_index,start_date,a_ratio,b_ratio,ratio_change,pred_start_date,pred_end_date]+out_slope
    out_slope = []
    if -999 in insert_data:
        pass
    else:
        df_out=df_out.append(pd.DataFrame(insert_data).T)


#print(df_out)
df_out.columns = ["stock_index","start_date","a_ratio","v_ratio","ratio_change","pred_start_date","pred_end_date"]+out_slope_name
#print(df_out)
df_out.round(3).to_csv("hk_increase_slope.csv",index=0)






