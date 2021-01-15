from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import *



data_dir="/home/davidyu/stock/data/dadan_real_time_ifeng/combine_data"
df1 = combine_csv_in_folder(data_dir)


df1.columns = ["stock_index","stock_name","trade_time",
    "price","trade_num","trade_shou","status",
    "price_change_rate","price_change_ratio","look","date"]

df2 = df1[df1["date"]!="date"]
df3 = df2.drop_duplicates()


df4 = df3[(df3["stock_index"]==600010)&(df3["trade_shou"]>100000)]








