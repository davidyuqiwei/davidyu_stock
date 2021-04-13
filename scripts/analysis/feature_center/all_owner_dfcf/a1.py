from davidyu_cfg import *
import pandas as pd
from functions.common.slope.dfcfStockSlope_date import *
from datetime import datetime,timedelta

def str_dates_add(str_date,add_day):
    a2=datetime.strptime(str_date, "%Y-%m-%d")+timedelta(days=add_day)
    return a2.strftime("%Y-%m-%d")


#owner_name = "香港中央结算有限公司"
owner_name = "全国社保"
#owner_name = "投资"
stat_days = 9

def cal_slope_after_report(owner_name,stat_days):
    df1 = pd.read_csv("/home/davidyu/stock/data/all_owner/history_data/dfcf_all_owner_2021-03-22.csv")
    #df2 = df1[df1["gudong_name"]==owner_name]
    df2 = df1.loc[df1["gudong_name"].str.contains(owner_name)]
    df3 = df2[["stock_index","stock_name","report_date","change_type"]].drop_duplicates()
    df3["stat_end_date"] = [str_dates_add(x,stat_days) for x in df3["report_date"].values.tolist()]
    #a1 = dfcfStockSlope(stock_index,start_date,end_date)
    slope_out = []
    rows_in = []
    for index,row in df3.iterrows():
        stock_index = str(row["stock_index"]).zfill(6)
        stat_start_date = row["report_date"]
        stat_end_date = row["stat_end_date"]
        a1 = dfcfStockSlope(stock_index,stat_start_date,stat_end_date,0)
        slope_out.append(a1.get("slope"))
        rows_in.append(a1.get("rows"))
    df3["slope"] = slope_out
    df3["slope_rows"] = rows_in
    return df3
#slope_days = df3['slope_rows'].mode().tolist()[0]
df3 = cal_slope_after_report(owner_name,stat_days)
slope_days = df3['slope_rows'].mode().tolist()[0]
df4 = df3[df3["slope_rows"]==slope_days]

df5 = df4[df4["change_type"]=="增加"]
print("增加")
print(df5[df5["slope"]>0].shape[0]/df5.shape[0])
print(df5.shape[0])


df5 = df4[df4["change_type"]=="新进"]
print("新进")
print(df5[df5["slope"]>0].shape[0]/df5.shape[0])
print(df5.shape[0])

df5 = df4[df4["change_type"]=="减少"]
print("减少")
print(df5[df5["slope"]>0].shape[0]/df5.shape[0])
print(df5.shape[0])


#df4 = df3[df3["slope_rows"]==]
#df5 = df4[df4["slope"]>0]








