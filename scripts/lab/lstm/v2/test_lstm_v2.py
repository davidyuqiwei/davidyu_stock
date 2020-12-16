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

def make_train_test_data(dataset,x_col_index,y_col_index):
    ds_shape = dataset.shape[1]
    # 将整型变为float
    dataset = dataset.astype('float32')
    #归一化 在下一步会讲解
    scaler = MinMaxScaler(feature_range=(0, 1))
    dataset = scaler.fit_transform(dataset)
    train_size = int(len(dataset) * 0.9)
    trainlist = dataset[:train_size]
    np.random.shuffle(trainlist)
    testlist = dataset[train_size:]
    y_train = np.array([x[y_col_index] for x in trainlist] )
    x_train = np.array([x[x_col_index] for x in trainlist])
    y_test = np.array([x[y_col_index] for x in testlist])
    x_test = np.array([x[x_col_index] for x in testlist])
    
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    return x_train,y_train,x_test,y_test,train_size


def xColIndex(df3,x_col_key):
    """
    give the key name , and return all the colum 
    index has the key
    """
    col_list = df3.columns.tolist()
    x_col_index = []
    for i in col_list:
        if any([x in i for x in x_col_key]):
            x_col_index.append(col_list.index(i))
    return x_col_index

def load_the_data(predict_days,history_days,future_predict_days):
    data_dir = "/home/davidyu/stock/data/test/for_lstm"
    file_name = "SH_index_price_mv_avg.csv"
    #shift_days = predict_days * -1
    df1 = read_mv_avg_data_clean(data_dir,file_name)
    ## add historical price as a new columns //  a new feature
    df1 = make_history_price(df1,history_days)  
    df1 = make_future_price(df1,future_predict_days)
    df2 = df1.dropna()[history_days+10:]
    #print(df2.shape)
    df3 = df2.dropna()
    x_col_key = ["adj_close","mv","HISTORY"]
    x_col_index = xColIndex(df3,x_col_key)
    y_col_key = ["FUTURE"]
    y_col_index = xColIndex(df3,y_col_key)
    df_model = df3.iloc[:,x_col_index+y_col_index]
    x_col_key = ["adj_close","mv","HISTORY"]
    x_col_index = xColIndex(df_model,x_col_key)
    y_col_key = ["FUTURE"]
    y_col_index = xColIndex(df_model,y_col_key)
    return df3,df_model,x_col_index,y_col_index

def train_model(df_raw,df_model,x_col_index,y_col_index):
    dataset = df_model.values
    x_train,y_train,x_test,y_test,train_size = make_train_test_data(dataset,x_col_index,y_col_index)
    model = load_model2(x_train,y_train)
    model.fit(x_train, y_train, epochs=20, batch_size=200, verbose=2)
    y_predict = model.predict(x_test)
    y_predict1 = [np.float(x[0]) for x in y_predict]
    y_test1 = [np.float(x[0]) for x in y_test]
    df1 = pd.DataFrame([y_test1, y_predict1]).T
    stock_date = df_raw["stock_date"][train_size:]
    df1["stock_date"] = stock_date.values
    mean_s_error = mean_squared_error(y_test1, y_predict1)
    print(mean_s_error)
    return df1
def load_model(x_train):
    model = Sequential()
    model.add(LSTM(60, input_shape=(x_train.shape[1], x_train.shape[2])))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model
def load_model2(x_train,y_train):
    model = Sequential()
    model.add(LSTM(32, input_shape=(x_train.shape[1], x_train.shape[2]),return_sequences=True))
    model.add(Dropout(0.1))
    model.add(LSTM(64,input_shape=(x_train.shape[1], x_train.shape[2]),return_sequences=False))
    model.add(Dropout(0.1))
    model.add(Dense(y_train.shape[1]))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

if __name__ == "__main__":
    predict_days = 7
    history_days = 30
    future_predict_days = 5
    df_raw,df_model,x_col_index,y_col_index = load_the_data(predict_days,history_days,future_predict_days)
    df1 = train_model(df_raw,df_model,x_col_index,y_col_index)
    df1.to_csv("test2.csv",index=0)

    #c=np.concatenate((x_test[0].reshape(1,-1),y_test[0].reshape(1,-1) ),axis=1)
    #c=np.concatenate((np.array([[0]*42]),y_test[0].reshape(1,-1)),axis=1)
    #scaler.inverse_transform(c)





