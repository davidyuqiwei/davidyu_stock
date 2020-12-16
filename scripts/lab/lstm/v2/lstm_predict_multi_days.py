#https://zhuanlan.zhihu.com/p/58825020
from __future__ import absolute_import, division, print_function, unicode_literals

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
from load_model_data import *
from davidyu_cfg import *
import sys
print(tf.__version__)
#from functions.models.davidCluster import *
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import metrics
from sklearn.metrics import explained_variance_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras.layers import Dropout

def make_train_test_data(dataset):
    ds_shape = dataset.shape[1]
    # 将整型变为float
    dataset = dataset.astype('float32')
    #归一化 在下一步会讲解
    scaler = MinMaxScaler(feature_range=(0, 1))
    dataset = scaler.fit_transform(dataset)
    train_size = int(len(dataset) * 0.8)
    trainlist = dataset[:train_size]
    testlist = dataset[train_size:]

    y_train = np.array([x[ds_shape-1] for x in trainlist] )
    x_train = np.array([x[0:(ds_shape-1)] for x in trainlist])
    y_test = np.array([x[ds_shape-1] for x in testlist])
    x_test = np.array([x[0:(ds_shape-1)] for x in testlist])
    
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    return x_train,y_train,x_test,y_test
def load_the_data(predict_days,history_days):
    data_dir = "/home/davidyu/stock/data/test/for_lstm"
    file_name = "SH_index_price_mv_avg.csv"
    shift_days = predict_days * -1
    df1 = read_mv_avg_data_clean(data_dir,file_name)
    ## add historical price as a new columns //  a new feature
    df1 = make_history_price(df1,history_days)  
    df2 = df1.dropna()[history_days+10:]
    print(df2.shape)
    df2['y'] = df2['adj_close'].shift(shift_days)
    df2 = make_future_price(df2,5)
    df3 = df2.dropna()
    df3 = df3.iloc[:,2:]
    dataset = df3.values
    x_train,y_train,x_test,y_test = make_train_test_data(dataset)
    
    model = load_model2(x_train)
    model.fit(x_train, y_train, epochs=20, batch_size=200, verbose=2)


    y_predict = model.predict(x_test)
    y_predict1 = [np.float(x[0]) for x in y_predict]
    df1 = pd.DataFrame([y_test, y_predict1]).T
    
    mean_s_error = mean_squared_error(y_test, y_predict1)
    print(mean_s_error)
    return df1
def load_model(x_train):
    model = Sequential()
    model.add(LSTM(60, input_shape=(x_train.shape[1], x_train.shape[2])))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model
def load_model2(x_train):
    model = Sequential()
    model.add(LSTM(60, input_shape=(x_train.shape[1], x_train.shape[2]),return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(60,input_shape=(x_train.shape[1], x_train.shape[2]),return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(4))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

if __name__ == "__main__":
    predict_days = 7
    history_days = 60
    df1 = load_the_data(predict_days,history_days)
    df1.to_csv("test.csv",index=0)


