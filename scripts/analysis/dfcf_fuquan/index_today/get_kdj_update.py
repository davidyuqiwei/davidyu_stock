from davidyu_cfg import *
#from functions.pyspark_functions import *
from functions.baostock.stock_return import *
from functions.common.loadModule.load_module_kdj import *
import pickle
from m_features import *
#data_dir = os.path.join(data_dict.get("dfcf_fuquan"),"parse_data")




def kdj_x(x):
    stock = DF_to_StockDataFrame(x)
    ss,tt = stock_kdj(stock)
    #print(ss)
    return ss


def last_row(x,sort_col):
    x1 = x.sort_values(sort_col).tail(1)
    return x1

def select_day(x,dt):
    x1 = x[x["dt"]==dt]
    return x1

def mv_avg(x,col='close',window=5):
    new_col = "mvavg"+str(window)
    x[new_col] = x[col].rolling(window).mean()
    return x


def new_col(x):
    print("new_col")
    for x1 in ["open","high","low","close"]:
        for y in ["mvavg3","mvavg5","mvavg8","mvavg13","mvavg21"]:
            x[x1+"_"+y] = x[x1]/x[y]
    x['mv_avg_3_5'] = x["mvavg3"]/x["mvavg5"]
    x['mv_avg_5_8'] = x["mvavg5"]/x["mvavg8"]
    x['mv_avg_3_8'] = x["mvavg3"]/x["mvavg8"]
    x['mv_avg_3_13'] = x["mvavg3"]/x["mvavg13"]
    return x


def tran_to_float(df2):
    df2["close"] = [ np.float(x) for x in df2["close"].values.tolist() ]
    df2["low"] = [ np.float(x) for x in df2["low"].values.tolist() ]
    df2["high"] = [ np.float(x) for x in df2["high"].values.tolist() ]
    df2["open"] = [ np.float(x) for x in df2["open"].values.tolist() ]
    return df2

def make_mv_avg(df2):
    print("make_mv_avg")
    df2 = df2.groupby("stock_index").apply(lambda x: mv_avg(x,window=3))
    df2 = df2.groupby("stock_index").apply(lambda x: mv_avg(x,window=5))
    df2 = df2.groupby("stock_index").apply(lambda x: mv_avg(x,window=8))
    df2 = df2.groupby("stock_index").apply(lambda x: mv_avg(x,window=13))
    df2 = df2.groupby("stock_index").apply(lambda x: mv_avg(x,window=21))
    return df2


def make_test_data(df3,feature_columns):
    df4 = df3.reset_index(drop=True)
    df4 = df4.dropna().round(3).drop_duplicates()
    #df5 = df4.groupby("stock_index").apply(lambda x: last_row(x,"dt"))
    df5 = df4.groupby("stock_index").apply(lambda x: select_day(x,"2021-01-25"))
    df6 = df5.reset_index(drop=True)
    feature_name = feature_columns
    df7 = df6[["stock_index","dt"]+feature_name]
    #-----------------------------------------------#
    #df7.to_csv("test_data.csv",index=0)
    test_data = df7[feature_name]
    return df7,test_data


def price_norm(df,col_list):
    for i in col_list:
        df[i] = df[i]/df[i].max()
    return df

def load_index_300():
    df_300 = pd.read_csv("/home/davidyu/stock/data/common/index_300_raw.txt",header=None)
    index_300 = [str(x[0]).zfill(6) for x in df_300.values.tolist()]
    return index_300

run_today_data = 1
test_data = 0
if run_today_data==1:
    data_dir = os.path.join(tmp_data_dict.get("dfcf_fuquan"))
    df1 = pd.read_csv(os.path.join(data_dir,"dfcf_fuquan.csv"))
    index_300 = load_index_300()
    df1 = df1[df1["stock_index"].isin(index_300)]
    df_raw = df1[df1["dt"]!="dt"].drop_duplicates()
    df2 = tran_to_float(df_raw)
    #
    if test_data ==1:
        df1 = df_raw[df_raw["stock_index"]=="601398"]
    #df2 = df1.copy(deep=True)
    df_norm = df2.copy(deep=True)
    df_norm = df2.groupby("stock_index").apply(lambda x: price_norm(x,["close","open","low","high"]))
    #index_300 = load_index_300()
    #df3 = df2.groupby("stock_index").apply(lambda x: kdj_x(x))
    df3 = df_norm.groupby("stock_index").apply(lambda x: kdj_x(x))
    df3["boll_ratio"] = df3["boll_ub"]/df3["boll_lb"]
    df3["macdh_sumavg5"] = df3["macdh"].rolling(5).sum()
    df3["macdh_sumavg10"] = df3["macdh"].rolling(10).sum()
    df5 = df3.reset_index(drop=True)
    df5 = df5.dropna().round(3).drop_duplicates()
    df5.to_csv("today_kdj_all.csv",index=0)

df5 = pd.read_csv("today_kdj_all.csv")
df6 = df5[df5["stock_date"]=="2021-01-25"]
df7 = df6[["stock_index","stock_date","rsi_6","macdh","macdh_sumavg5","macd","macds"]]
df7.sort_values("rsi_6").to_csv("rsi6_sort_today.csv",index=0)
df7["macdh_abs"] = df7["macdh"].abs()
df8 = df7[df7["macdh_mvavg5"]<0]
df8.round(3).sort_values("macdh_abs").to_csv("macdh_sort_today.csv",index=0)
df8.round(3).sort_values("macd").to_csv("macd_sort_today.csv",index=0)



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

