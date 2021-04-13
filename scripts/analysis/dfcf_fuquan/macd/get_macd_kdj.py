from davidyu_cfg import *
#from functions.pyspark_functions import *
from functions.baostock.stock_return import *
from functions.common.loadModule.load_module_kdj import *
## new macd parameter
from functions.common.macd_kdj.get_kdj import *
import pickle
#from m_features import *
#data_dir = os.path.join(data_dict.get("dfcf_fuquan"),"parse_data")

def load_index_300():
    df_300 = pd.read_csv("/home/davidyu/stock/data/common/index_300_raw.txt",header=None)
    index_300 = [str(x[0]).zfill(6) for x in df_300.values.tolist()]
    return index_300




def load_today_dfcf_data(stock_index):
    #data_dir = os.path.join(tmp_data_dict.get("dfcf_fuquan"))
    data_file = "/home/davidyu/stock/data/history_data/dfcf_fuquan/stock_index/"+stock_index+"_fuquan.csv"
    df1 = pd.read_csv(data_file)
    df1 = df1[df1["dt"]!="dt"].drop_duplicates()
    return df1


def df_macd_para(df2):
    df3 = df2.groupby("stock_index").apply(lambda x: kdj_x(x)).reset_index(drop=True)
    df3 = df3.groupby("stock_index").apply(lambda x: new_kdj(x,16,3,3)).reset_index(drop=True)
    df3 = df3.groupby("stock_index").apply(lambda x: new_macd(x,'close',5,34,5)).reset_index(drop=True)
    df3 = df3.groupby("stock_index").apply(lambda x: new_macd(x,'close',13,55,8)).reset_index(drop=True)
    df3["boll_ratio"] = df3["boll_ub"]/df3["boll_lb"]
    df3["macdh_mvavg5"] = df3["macdh"].rolling(5).mean()
    

    df3["low_mean"]=pd.Series.rolling(df3["low"],window=20).mean()
    df3["low_std"]=pd.Series.rolling(df3["low"],window=20).std()
    df3["high_std"]=pd.Series.rolling(df3["high"],window=20).std()
    df3["high_mean"]=pd.Series.rolling(df3["high"],window=20).mean()
    
    df3["boll_high_up"] = df3["high_mean"]+2*df3["high_std"]
    df3["boll_high_down"] = df3["high_mean"]-2*df3["high_std"]
    df3["boll_low_up"] = df3["low_mean"]+2*df3["low_std"]
    df3["boll_low_down"] = df3["low_mean"]-2*df3["low_std"]
    return df3
def calcluate_parameters(stock_index,test_data_input=1):
    run_today_data = 1
    test_data = test_data_input
    if run_today_data==1:
        # load data
        df1 = load_today_dfcf_data(stock_index)
        if test_data ==1:
            df1 = df1[df1["stock_index"]=="601398"]
        df2 = df1.copy()
        df2 = tran_to_float(df2)
        df3 = df_macd_para(df2)
    
        df5 = df3.reset_index(drop=True)
        df5 = df5.dropna().round(3).drop_duplicates()
    return df5
stock_index="000016"


df3 = calcluate_parameters(stock_index,test_data_input=0)
df_roll_slope = pd.read_csv("/home/davidyu/stock/data/feature_center/rolling_regression/stock_index/5days_update/"+stock_index+"_roll_reg_5.csv")
df_all = pd.merge(df3,df_roll_slope,how='inner',on='dt')

df_all["low_boll_low_down"] = df_all["low"]-df_all["boll_low_down"]
df_all["low_boll_low_down_dir"] =0
df_all["low_boll_low_down_dir"][df_all["low_boll_low_down"]>0] =1
df_all["slope_dir"] = 0
df_all["slope_dir"][df_all["slopes"]>0] = 1

df_all_save = df_all[["low","boll_low_down","macdh",'kdjk', 'kdjd', 'kdjj',"rsi_6","rsi_12","slopes",
    "slope_dir","low_boll_low_down","low_boll_low_down_dir","dt"]]
df_all_save = df_all_save[df_all_save["dt"]>"2013-01-01"]
df_all_save.round(3).to_csv("data_out.csv",index=0)


df_all1 = df_all[df_all["low"]<df_all["boll_low_down"]]
df_all2 = df_all1[["low","boll_low_down","macdh","rsi_6","rsi_12","slopes","dt"]]

df_all3 = df_all2[df_all2["dt"]>="2016-01-01"]
df_all3["low_boll_low_down_ratio"] = df_all["low"]/df_all["boll_low_down"]
print(df_all3[df_all3["slopes"]>0].shape)
print(df_all3[df_all3["slopes"]<0].shape)
print(df_all3[df_all3["slopes"]>0])
print(df_all3[df_all3["slopes"]<0])
#print(df_all3)


# save data        
#df5 = calcluate_parameters(test_data_input=0)
#df5 = df5.rename(columns={'stock_date':'dt'})
#df5.to_csv("today_kdj_hs_300.csv",index=0)













'''
df5 = pd.read_csv("today_kdj_all.csv")
df6 = df5[df5["stock_date"]=="2021-01-25"]
df7 = df6[["stock_index","stock_date","rsi_6","macdh","macdh_mvavg5","macd","macds"]]
df7.sort_values("rsi_6").to_csv("rsi6_sort_today.csv",index=0)
df7["macdh_abs"] = df7["macdh"].abs()
df8 = df7[df7["macdh_mvavg5"]<0]
df8.round(3).sort_values("macdh_abs").to_csv("macdh_sort_today.csv",index=0)
df8.round(3).sort_values("macd").to_csv("macd_sort_today.csv",index=0)

'''



"""

df7,test_data = make_test_data(df5,feature_columns)

import xgboost as xgb
with open('scaler.pickle', 'rb') as f: ss = pickle.load(f)
xgb_m = xgb.Booster(model_file='xgb_index_base.model')
test_data1 = ss.transform(test_data)

test_data2=pd.DataFrame(test_data1)
test_data2.columns = feature_columns
xgb_out = xgb_m.predict(xgb.DMatrix(test_data2)).tolist()

df_out = pd.DataFrame(xgb_out)
df_out["stock_index"] = df7["stock_index"]
df_out["dt"] = df7["dt"]
df_out.columns = ["val","stock_index","dt"]
print(df_out.sort_values("val",ascending=False).head(30))
#df_out.to_csv("out_index_today",index=0)

#with open('scaler.pickle', 'rb') as f: ss = pickle.load(f)

df_300 = pd.read_csv("/home/davidyu/stock/data/common/stock_list_test.txt",header=None)
index_300 = [str(x[0]).zfill(6) for x in df_300.values.tolist()] 
df_out[df_out["stock_index"].isin(index_300)].sort_values("val").tail(30)
"""

