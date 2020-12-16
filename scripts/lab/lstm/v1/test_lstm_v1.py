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
from functions.models.davidCluster import *
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import metrics
from sklearn.metrics import explained_variance_score

def load_the_data():
    data_dir = "/home/davidyu/stock/data/test/for_lstm"
    file_name = "SH_index.csv"
    df1 = read_mv_avg_data_clean(data_dir,file_name)
    history_days = 30
    df1 = make_history_price(df1,history_days)  
    ## add historical price as a new columns //  a new feature
    df1 = make_history_vol(df1,history_days)
    df2 = df1.dropna()[2300:]
    df2['y'] = df2['adj_close'].shift(-1)
    df3 = df2.dropna()
    feature_list = df3.columns[3:86].tolist()
    Y = df3.y.values
    X = df3[feature_list].values
    
    min_max_scaler = preprocessing.MinMaxScaler()
    x_minmax = min_max_scaler.fit_transform(X)
    y_minmax = min_max_scaler.fit_transform(Y.reshape(-1,1))
    
    x_train, x_test, y_train, y_test = train_test_split(x_minmax, y_minmax, test_size=.3)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    model = load_model(x_train,y_train):
    y_predict = model.predict(x_test)
    y_test1 = [np.float(x[0]) for x in y_test]   
    y_predict1 = [np.float(x[0]) for x in y_predict]

    df1 = pd.DataFrame([y_test1, y_predict1]).T
    return  train_X,train_y,test_X,test_y,y_min,y_max


def load_model(x_train,y_train):
    model = Sequential()
    model.add(LSTM(4, input_shape=(x_train.shape[1], x_train.shape[2])))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(x_train, y_train, epochs=10, batch_size=500, verbose=2)
    return model


def load_model2(input_shape1):
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.LSTM(8,input_shape=(None, input_shape1),return_sequences=True))
    model.add(tf.keras.layers.Dropout(0.2))
    #model.add(tf.keras.layers.LSTM(8,input_shape=(None, input_shape1),return_sequences=True))
    #model.add(tf.keras.layers.Dropout(0.2))
    model.add(tf.keras.layers.LSTM(32))
    model.add(layers.Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam',
         loss='mae',
         metrics=['accuracy'])
    return model

train_X,train_y,test_X,test_y,y_min,y_max = load_the_data()
input_shape1 = train_X.shape[2]
#model = load_model(input_shape1)
model = load_model2(input_shape1)
 

history = model.fit(train_X, train_y, 
     validation_data=(test_X, test_y),batch_size=32,epochs=100)

def model_result(model):
    result = model.predict(test_X, batch_size=32)
    result_list = [x[0] for x in result]
    
    data_dict = {
        "test_y": test_y.tolist(),
        "test_y_predict": result_list
        }
    from sklearn.metrics import mean_squared_error
    mean_s_error = mean_squared_error(test_y,result_list)
    print(mean_s_error)
    abs_error = np.sum(np.abs(test_y-result_list))
    print(abs_error)
    df_pred_out = pd.DataFrame(data_dict)
    print(df_pred_out.head())
    return df_pred_out


df_pred_out = model_result(model)
df_pred_out.to_csv("pred_8_32.csv",index=0)

