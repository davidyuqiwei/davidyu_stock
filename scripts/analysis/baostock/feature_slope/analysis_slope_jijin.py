from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import *

raw_data_dir = tmp_data_dict.get("baostock")



#df1 = pd.read_csv("dadan_slope.csv",header=None)
#df_dadan = pd.read_csv(os.path.join(raw_data_dir,"feature_slope","dadan_data.csv"),header=None)
#df_dadan.columns = ["stock_index","dadan_date","dadan_money"]

df_raw = pd.read_csv(os.path.join(raw_data_dir,"feature_slope","jijin_data.csv"),header=None)
df_raw.columns = ["stock_index","stock_date","stock_name","jijin_num"]
df1 = pd.read_csv("jijin_slope.txt",header=None)



df1.columns = ["stock_index","stock_date","pred_end_date","pred_days","slope"]

#df_merge1 = pd.merge(df_raw,df1,how="inner",on=["stock_index","stock_date"])
df_merge1 = pd.merge(df_raw,df1,how="inner",on=["stock_index"])
#def
df2 = df_merge1[df_merge1["slope"]!=-999]
df2.groupby("pred_days").mean()
df2.groupby("pred_days")["slope"].mean()


df2["jijin_num"]

df2["jijin_num_cut"] = pd.cut(df2['jijin_num'],bins=[0,100,200,500,1500,3000])


df_avg_slope = df2.groupby(["jijin_num_cut","pred_days"])["slope"].mean().reset_index()
#df_avg_slope.to_csv("df_avg_slope.csv",index=0)



#df2.groupby("pred_days").median()


