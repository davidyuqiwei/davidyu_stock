from davidyu_cfg import *
#from functions.pyspark_functions import *
from functions.baostock.stock_return import *
from functions.common.loadModule.load_module_kdj import *
import pickle
from functions.common.macd_kdj.m_features import *
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

def new_kdj(df,kdj_day=9,k_stat=3,d_stat=3):
    low_list = df['low'].rolling(kdj_day, min_periods=kdj_day).min()
    low_list.fillna(value = df['low'].expanding().min(), inplace = True)
    high_list = df['high'].rolling(kdj_day, min_periods=kdj_day).max()
    high_list.fillna(value = df['high'].expanding().max(), inplace = True)

    rsv = (df['close'] - low_list) / (high_list - low_list) * 100
    new_str = '_'.join([str(kdj_day),str(k_stat),str(d_stat)])
    k_col = 'K_'+new_str
    d_col = 'D_'+new_str
    j_col = 'J_'+new_str
    df['K'] = pd.DataFrame(rsv).ewm(com=k_stat-1).mean()
    df[k_col] = pd.DataFrame(rsv).ewm(com=k_stat-1).mean()
    df['D'] = df['K'].ewm(com=d_stat-1).mean()
    df[d_col] = df['K'].ewm(com=d_stat-1).mean()
    df[j_col] = 3 * df['K'] - 2 * df['D']
    return df

def new_macd(df2,col,MACD_EMA_SHORT = 12,MACD_EMA_LONG = 26, MACD_EMA_SIGNAL = 9):
    fast=df2[col].ewm(
                ignore_na=False, span=MACD_EMA_SHORT,
                min_periods=0, adjust=True).mean()
    slow=df2[col].ewm(
                ignore_na=False, span=MACD_EMA_LONG,
                min_periods=0, adjust=True).mean()
    # df2["volume_26"].plot(secondary_y=True, style='r*-')
    # df2["volume_12"].plot(secondary_y=True, style='b*-')
    new_str = '_'.join([str(MACD_EMA_SHORT),str(MACD_EMA_LONG),str(MACD_EMA_SIGNAL)])
    new_macd_col = 'macd_'+new_str
    new_macds_col = 'macds_'+new_str
    new_macdh_col =  'macdh_'+new_str
    df2[new_macd_col] = fast-slow
    df2[new_macds_col] = df2[new_macd_col].ewm(
                ignore_na=False, span=MACD_EMA_SIGNAL,
                min_periods=0, adjust=True).mean()
    df2[new_macdh_col] = (df2[new_macd_col] - df2[new_macds_col])
    return df2





