import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.utils import np_utils
import os
from load_model_data import *


file1 = "/home/davidyu/stock/data/test/longterm_sample_data.csv"
df1 = pd.read_csv(file1,sep="\t")
df1.columns = [x.split('.')[1] for x in df1.columns.tolist()]


df2 = df1.groupby('stock_index').apply(make_history_price,history_days=30)
df3 = df2.groupby('stock_index').apply(make_history_vol,history_days=30)

start_index = df3.columns.tolist().index('close1')
feature_index = [x for x in range(start_index,df3.shape[1])]
index_in = [6]+feature_index
df_model_raw = df3.iloc[:,index_in]
df_model = df_model_raw.dropna()
df_X = df3.iloc[:,start_index:]
df_Y = df3['adj_close']


make_history_vol(df1,history_days)

