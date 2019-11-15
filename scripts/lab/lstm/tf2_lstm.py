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
    file_name = "SH_index.csv"
    df1 = read_mv_avg_data_clean(data_dir,file_name)
    history_days = 30
    df1 = make_history_price(df1,history_days)
    train_nums = 4000
    y_start = 2
    train_X,train_y,test_X,test_y,y_min,y_max = make_train_test_data(df1,train_nums,y_start)
    return  train_X,train_y,test_X,test_y,y_min,y_max


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
    model.add(tf.keras.layers.LSTM(32,input_shape=(None, input_shape1)))
    model.add(layers.Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam',
         loss='mae',
         metrics=['accuracy'])
    return model

train_X,train_y,test_X,test_y,y_min,y_max = load_the_data()
input_shape1 = train_X.shape[2]
#model = load_model(input_shape1)
model = load_model2(input_shape1)
 
'''
BATCH_SIZE = 32
BUFFER_SIZE = 1

train_univariate = tf.data.Dataset.from_tensor_slices((train_X,train_y))
train_univariate = train_univariate.cache().shuffle(BUFFER_SIZE).batch(BATCH_SIZE).repeat()

val_univariate = tf.data.Dataset.from_tensor_slices((test_X, test_y))
val_univariate = val_univariate.batch(BATCH_SIZE)

EPOCHS = 10
EVALUATION_INTERVAL = 10
model.fit(train_univariate,epochs=EPOCHS,
        steps_per_epoch=EVALUATION_INTERVAL,
        validation_data=val_univariate, validation_steps=20)

'''

history = model.fit(train_X, train_y, 
     validation_data=(test_X, test_y),batch_size=32,epochs=10)

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

'''
history = model.fit(train_X, train_y, 
     validation_data=(test_X, test_y),batch_size=32,epochs=10,
     callbacks=[cp_callback])

'''


model_result(model)


'''
curr_dir = "/home/davidyu/stock/scripts/davidyu_stock/scripts/lab/lstm"
checkpoint_path = os.path.join(curr_dir,"training_1/cp-{epoch:04d}.ckpt")

cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1,
                                                 period=5)

'''


'''
history = model2.fit(train_X, train_y, 
     validation_data=(test_X, test_y),batch_size=32,epochs=10,
     callbacks=[cp_callback])
model_result(model2)

'''
#df_out = pd.DataFrame(data_dict)

#df_out.to_csv("test.csv")






#result = model.predict(train_x, batch_size=32)
#print(result)
