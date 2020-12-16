from davidyu_cfg import *
import pandas as pd
from functions.baostock.stock_slope import *
def get_out_slope_name(pred_days_list):
    out_slope_name = []
    for pred_days in pred_days_list:
        slope_name = "slope_"+str(pred_days)
        out_slope_name.append(slope_name)
    return out_slope_name
#for i in range(0,10):
def get_df_out(df1,pred_days_list):
    out_slope = []
    df_out = pd.DataFrame()
    for i in range(0,df1.shape[0]):
        for pred_days in pred_days_list:
            stock_index = str(df1["stock_index"][i]).zfill(6)
            start_date = df1["dadan_date"][i]
            dadan_vol = df1["vol"][i]
            slope,pred_start_date,pred_end_date = stockSlope(stock_index,start_date,stat_days,pred_days)
            out_slope.append(slope)
        insert_data = [stock_index,start_date,dadan_vol,pred_start_date,pred_end_date]+out_slope
        out_slope = []
        if -999 in insert_data:
            pass
        else:
            df_out=df_out.append(pd.DataFrame(insert_data).T)
    return df_out

df1 = pd.read_csv("dadan_data.csv",header=None)
df1.columns = ["stock_index","dadan_date","vol"]
stat_days = 1
pred_days = 30
pred_days_list = [5,10,15,20,30]
out_slope_name = get_out_slope_name(pred_days_list)
#print(df_out)
df_out = get_df_out(df1,pred_days_list)
df_out.columns = ["stock_index","start_date","dadan_vol","pred_start_date","pred_end_date"]+out_slope_name
print(df_out)
#df_out.to_csv("dadan_slope.csv",index=0)





