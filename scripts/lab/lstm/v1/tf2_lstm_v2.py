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
import sys
print(tf.__version__)

def load_the_data():
    data_dir = "/home/davidyu/stock/data/test/for_lstm"
    file_name = "SH_index_price_mv_avg.csv"
    df1 = read_mv_avg_data_clean(data_dir,file_name)
    history_days = 30
    df1 = make_history_price(df1,history_days)
    #df1 = make_history_vol(df1,history_days)
    #df1 = df1.drop(columns=['volume'])
    #df1['adj_close_raw'] = df1['adj_close']
    df1['adj_close'] = df1['adj_close'].shift(-1)
    ## remove first xx rows,like 300 rows, becuase moving average, it doesnt have data
    train_nums = 4000
    start_index = 2
    feature_start_index = 2
    train_X,train_y,test_X,test_y,y_min,y_max = make_train_test_data(df1,
            start_from_num,
            train_nums,
            start_index,
            feature_start_index)
    test_X = test_X[:-1]  # remove the last one for predict
    test_y = test_y[:-1]
    x_for_predict = test_X[-1:]
    return  train_X,train_y,test_X,test_y,y_min,y_max,x_for_predict


def load_model(input_shape1):
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.LSTM(8,input_shape=(None, input_shape1),return_sequences=True))
    model.add(tf.keras.layers.Dropout(0.2))
    #model.add(tf.keras.layers.LSTM(32))
    model.add(tf.keras.layers.LSTM(100, return_sequences=False))
    model.add(layers.Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam',
         loss='mae',
         metrics=['accuracy'])
    return model


def load_model2(input_shape1):
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.LSTM(50,input_shape=(None, input_shape1),return_sequences=True))
    model.add(tf.keras.layers.LSTM(50,input_shape=(None, input_shape1)))
    model.add(layers.Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam',
         loss='mean_squared_error',
         metrics=['accuracy'])
    return model


def model_result(model):
    result = model.predict(test_X, batch_size=32)
    result_list = [x[0] for x in result]
    data_dict = {
        "test_y": test_y.tolist(),
        "test_y_predict": result_list
        }
    from sklearn.metrics import mean_squared_error
    mean_s_error = mean_squared_error(test_y,result_list)
    print("the mean square error is %.2f" %mean_s_error)
    abs_error = np.sum(np.abs(test_y-result_list))
    print("the sum absolute error is %.2f" %abs_error)
    df_pred_out = pd.DataFrame(data_dict)
    #print(df_pred_out.head())
    return df_pred_out


train_X,train_y,test_X,test_y,y_min,y_max,x_for_predict = load_the_data()
input_shape1 = train_X.shape[2]
#model = load_model(input_shape1)
model = load_model2(input_shape1)
 

history = model.fit(train_X, train_y, 
        validation_data=(test_X, test_y),batch_size=1,epochs=5,verbose=2)

pred_df = model_result(model)
pred_df.to_csv("pred_df.csv",index=0)
predict_y = model.predict(x_for_predict, batch_size=32)
#predict_y = model.predict(x_for_predict)

def get_pred_raw(predict_y):
    pred_raw = predict_y*(y_max-y_min)+y_min
    pred_raw_num = pred_raw[0][0]
    return pred_raw_num
pred_raw_num = get_pred_raw(predict_y)
print("the predict for next day is %.2f" %pred_raw_num)
corr1 = pred_df.test_y.corr(pred_df.test_y_predict)
print("the predict correlation is %.2f" %corr1)






