from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import *



data_dir="/home/davidyu/stock/data/dadan_real_time_ifeng/combine_data"
file_in = "2021-01-18.csv"

df1 = pd.read_csv(os.path.join(data_dir,file_in))

df1.columns = ["stock_index","stock_name","trade_time",
    "price","trade_money_wan","trade_shou","status",
    "price_change_rate","price_change_ratio","look","date"]

df1.to_csv("dd_realtime.csv",index=0)
'''
df2 = df1[df1["date"]!="date"]
df3 = df2.drop_duplicates()


df4 = df3[(df3["stock_index"]==600010)&(df3["trade_money_wan"]>500)]
df4 = df3[(df3["trade_money_wan"]>500)]

df4.groupby("stock_index").count()["stock_name"]

df5 = df4.groupby("stock_index").count()["stock_name"].reset_index().sort_values("stock_name")





df4 = df3[(df3["trade_"]>100000)]

'''








