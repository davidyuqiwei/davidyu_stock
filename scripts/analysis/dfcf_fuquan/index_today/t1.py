from davidyu_cfg import *
#from functions.pyspark_functions import *
from functions.baostock.stock_return import *
from functions.common.loadModule.load_module_kdj import *
import pickle
from m_features import *

def kdj_x(x):
    stock = DF_to_StockDataFrame(x)
    ss,tt = stock_kdj(stock)
    #print(ss)
    return ss

def load_index_300():
    df_300 = pd.read_csv("/home/davidyu/stock/data/common/index_300_raw.txt",header=None)
    index_300 = [str(x[0]).zfill(6) for x in df_300.values.tolist()]
    return index_300

def price_norm(df,col_list):
    for i in col_list:
        df[i] = df[i]/df[i].max()
    return df


index_300 = load_index_300()
data_all = []
for i in index_300:
    try:
        file_in = "/home/davidyu/stock/data/history_data/dfcf_fuquan/stock_index/%s_fuquan.csv"%(i)
        slope_file = "/home/davidyu/stock/data/feature_center/rolling_regression/stock_index/dfcf_fuquan_sample_data/%s_roll_reg_3.csv"%(i)
        df1 = pd.read_csv(file_in)
        
        df_norm = df1.groupby("stock_index").apply(lambda x: price_norm(x,["close","open","low","high"]))
        df2 = kdj_x(df_norm)
        df_slope = pd.read_csv(slope_file)
        
        df_m1 = pd.merge(df2,df_slope,on=["dt"])
        df_m2 = df_m1[df_m1["slope_num_in"]==df_m1["days_default"]]
        df_m3 = df_m2.dropna()
        
        df_m3["macdh_mvavg5"] = df_m3["macdh"].rolling(5).mean()
        df_m3["macdh_mvavg3"] = df_m3["macdh"].rolling(3).mean()
        df_m3["macdh_mvavg10"] = df_m3["macdh"].rolling(10).mean()
        
        df_m3["macdh_up"] = df_m3["macdh"]/df_m3["macdh"].abs().rolling(5).mean()
        df_m3 = df_m3.dropna()
        data_all.append(df_m3)
    except:
        pass
#df_m3.to_csv("macd_test.csv",index=0)
data_all1 = pd.concat(data_all)
data_all1 = data_all1[data_all1["dt"]>="2020-01-01"]
data_all1.round(3).drop_duplicates().to_csv("macd_test.csv",index=0)
