from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *

now_date,now_date_time = get_the_datetime()

dir_dadan = data_dict.get("DADAN")
data_dir = os.path.join(dir_dadan,now_date)
df1 = combine_csv_in_folder(data_dir)
df1.columns = ["stock_index","stock_name","trade_time",
"price","trade_num","trade_shou","status",
"price_change_rate","price_change_ratio","look"]

#print(df1.shape)
df2 = df1.drop_duplicates()
df2 = df2[df2["status"] == "买盘"]
df3 = df2.groupby(["stock_index","stock_name"]).count().sort_values("status",ascending=False)
#print(df2.shape)
print(df3.head(50))
print(df3.tail(50))


