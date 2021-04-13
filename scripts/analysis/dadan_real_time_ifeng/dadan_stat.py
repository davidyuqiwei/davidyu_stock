from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import *
from functools import reduce
from functions.common.cleanData import *


data_dir="/home/davidyu/stock/data/dadan_real_time_ifeng/combine_data"
files = os.listdir(data_dir)

file_in = "2021-01-18.csv"
data_all_list = []
for file_in in files:
    df1 = pd.read_csv(os.path.join(data_dir,file_in))
    df1.columns = ["stock_index","stock_name","trade_time",
        "price","trade_money_wan","trade_shou","status",
        "price_change_rate","price_change_ratio","look","date"]
    df2 = df1[df1["date"]!="date"]
    df3 = df2.drop_duplicates()
    #df3[df3["trade_time"]>="14:50:00"]
    #df4 = df3[(df3["stock_index"]==600010)&(df3["trade_money_wan"]>500)]
    df4 = df3[(df3["trade_money_wan"]>500)]
    df5 = df4.groupby("stock_index").count()["stock_name"].reset_index().sort_values("stock_name")
    df5.columns = ["stock_index","dadan_cnt"]
    df5["dt"] = file_in[0:10]
    data_all_list.append(df5)

df6 = pd.concat(data_all_list)

a1 = df6.groupby("stock_index").sum().reset_index()
a2 = df6.groupby("stock_index").agg({'dt': pd.Series.nunique}).reset_index().rename(columns={'dt':'dt_cnt'})
a5 = df6.groupby("stock_index").agg({'dt': max}).reset_index().rename(columns={'dt':'last_date'})
dfs = [a1,a2,a5]
a3 = reduce(lambda left,right: pd.merge(left,right,on='stock_index',how='left'), dfs)
a3["avg_daily_dadan_cnt"] = a3["dadan_cnt"]/a3["dt_cnt"]
#a3.sort_values("avg_daily_dadan_cnt")
a3 = cleanData.changeStockIndex(a3,"stock_index")
a3["stock_index"] = 's'+a3["stock_index"]
a3.round(0).to_csv("realtime_dadan_stat.csv",index=0)
#df4 = df3[(df3["trade_"]>100000)]








