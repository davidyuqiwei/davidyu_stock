import pandas as pd
#from keras.models import Sequential
#from keras.layers import Dense
#from keras.layers import LSTM
#from keras.utils import np_utils
import os
from davidyu_cfg import *
from load_model_data import *
from functions.LinearReg import LinearReg
from functions.rolling_regression import *

def df_first_N(x,N_days):
    n_days = -1*N_days
    df1 = x.sort_values("stock_date")
    df2 = df1.iloc[n_days:,:]
    return df2

def make_model_data(data_file,historical_days,regression_days):
    df_raw = pd.read_csv(data_file,sep="\t")
    df_raw.columns = [x.split('.')[1] for x in df_raw.columns.tolist()]
    df1 = df_raw.groupby('stock_index').apply(df_first_N,N_days=2000)
    df1.index = [x for x in range(0,df1.shape[0])]
    #----  historical stock price --- #
    df2 = df1.groupby('stock_index').apply(make_history_price,history_days=historical_days)
    #---- add historical volume -----#
    df3 = df2.groupby('stock_index').apply(make_history_vol,history_days=historical_days)
    ## rolling regression and sort by stock_date
    sort_col = "stock_date"
    df4 = df3.groupby('stock_index').apply(rolling_regression, \
        window=5,sort_col=sort_col,reg_col="adj_close")
    df4.to_csv('raw_sample_data.csv',index=0)

data_file = "/home/davidyu/stock/data/test/longterm_sample_data_mv_avg.csv"
historical_days = 30
regression_days = 10
make_model_data(data_file,historical_days,regression_days)


