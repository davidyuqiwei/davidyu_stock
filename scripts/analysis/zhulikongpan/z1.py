from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import *



now_date,_ = get_the_datetime()



#datetime.datetime.strptime(now_date,"%Y-%m-%d").date()
a1 = datetime.datetime.strptime(now_date,"%Y-%m-%d").date()-datetime.timedelta(7)
start_date = a1.strftime("%Y-%m-%d")


now_date = "2021-03-17"
data_dir = os.path.join(data_path,"history_data","zhulikongpan")
#files = os.path.join(data_dir,"zhulikongpan_2021-01-09.csv")
files = os.path.join(data_dir,"zhulikongpan_"+now_date+ ".csv")

df1 = pd.read_csv(files,header=None)

col_in = ["stock_date","stock_index","stock_name","new_price","x1","x2",
        "x3","zhuli_1_price","zhuli_ratio","zhuli_status","zhuli_20_price","a1","a2","a3",
        "a4","a5","a6","a7","a8","a9","a10","a11"]

df1.columns = col_in


df2 = df1[df1["zhuli_status"]=='完全控盘']
df2["stock_date"] = [x[0:10] for x in df2["stock_date"].values.tolist()]
df3 = df2[["stock_date","stock_index","stock_name","zhuli_ratio","zhuli_status"]]
df4 = df3.sort_values("zhuli_ratio",ascending=False).head(50)
print(df4)


# zhuli ratio avg

#df_zl_history = pd.read_csv("/home/davidyu/stock/data/tmp/zhulikongpan.csv",header=None)
#df_zl_history.columns = col_in
#df_zl_history["stock_date"] = [x[0:10] for x in df_zl_history["stock_date"].values.tolist()]
#df_stat = df_zl_history[(df_zl_history["stock_date"]>=start_date)&(df_zl_history["stock_date"]<=now_date)]
#df_zhuli_ratio_mean = df_stat.groupby("stock_index").mean()["zhuli_ratio"].reset_index()
#df_zhuli_ratio_mean = df_zhuli_ratio_mean.sort_values("zhuli_ratio",ascending=False).head(30)
#print(df_zhuli_ratio_mean)





