from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *

now_date,now_date_time = get_the_datetime()

dir_dadan = data_dict.get("DADAN")
#data_dir = os.path.join(dir_dadan,now_date)
data_dir = "/home/davidyu/stock/data/DADAN/"


os.system("find %s | xargs cat  * > all.csv" %data_dir)
os.system("sed -e '/0,1,2/d'  %sall.csv  > %sa.log" %(data_dir,data_dir))

df1 = combine_csv_in_folder(data_dir)
df1.columns = ["stock_index","stock_name","trade_time",
"price","trade_num","trade_shou","status",
"price_change_rate","price_change_ratio","look"]

#print(df1.shape)
df2 = df1.drop_duplicates()

df3 = df2[df2["status"] == "买盘"]
#df3 = df2.groupby(["stock_index","stock_name"]).count().sort_values("status",ascending=False)
df4 = df2.groupby(["stock_index","stock_name"])["trade_shou"].sum().reset_index()
df4.columns = ["stock_index","stock_name","buy_num"]
df5 = df2[df2["status"] == "卖盘"]
df6 = df5.groupby(["stock_index","stock_name"])["trade_shou"].sum().reset_index()
df6.columns = ["stock_index","stock_name","sale_num"]

#df4.join(df6,on=["stock_index","stock_name"])
df_merge = pd.merge(df4,df6,how='left',on = ["stock_index","stock_name"])
df_merge["buy_sale_diff"] = df_merge["buy_num"]-df_merge["sale_num"]
df_merge1 = df_merge.sort_values("buy_sale_diff",ascending=False)
df_merge1.to_csv("test.csv",encoding="utf_8_sig")
#print(df_merge1)

