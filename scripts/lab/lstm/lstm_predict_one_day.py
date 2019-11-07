#https://blog.csdn.net/u012735708/article/details/82769711
'''
@update time 2019.11.1
'''
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.utils import np_utils
import os 


def read_mv_avg_data_clean(data_dir,file_name):
    '''
    this function read the moving average data
    '''
    data_dir = "/home/davidyu/stock/data/test/for_lstm"
    df1 = pd.read_csv(os.path.join(data_dir,file_name))
    df1 = df1.dropna().round(2)
    name_forward_string = df1.columns[0].split(".")[0]+"."
    df1.columns = [x.replace(name_forward_string,"") for x in df1.columns.tolist()]
    df1 = df1.sort_values("stock_date").reset_index()
    return df1


def make_history_price(df1,history_days):
    '''
    make shift days price 
    @return close1,close2,close3   -->  1day before, 2day before, 3day before
    '''
    for i in range(1,history_days):
        col_name = "close"+str(i)
        df1[col_name] = df1.adj_close.shift(i)
    return df1



def make_train_test_data(df1,train_nums,start_index):
    df_models_raw = df1.iloc[:,start_index:]
    df_models = (df_models_raw-df_models_raw.min())/(df_models_raw.max()-df_models_raw.min())
    df_X = df_models.iloc[400:df_models.shape[0],[i for i in range(1,df_models.shape[1])]]
    df_Y = df_models.iloc[400:df_models.shape[0],0]
    all_x_values = df_X.values
    all_y_values = df_Y.values
    train_X = all_x_values[:train_nums, :]
    train_y = all_y_values[:train_nums]
    test_X = all_x_values[train_nums:, :]
    test_y = all_y_values[train_nums:]
    train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
    test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
    y_min = df_models_raw.min()[0]
    y_max = df_models_raw.max()[0]
    return train_X,train_y,test_X,test_y,y_min,y_max
def make_model():
    model = Sequential()
    model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2])))
    model.add(Dense(1))
    model.compile(loss='mae', optimizer='adam')
    return model



data_dir = "/home/davidyu/stock/data/test/for_lstm"
file_name = "SH_index.csv"
df1 = read_mv_avg_data_clean(data_dir,file_name)
history_days = 30
df1 = make_history_price(df1,history_days)
train_nums = 4000
y_start = 2
train_X,train_y,test_X,test_y,y_min,y_max = make_train_test_data(df1,train_nums,y_start)

test_y_len = len(test_y)-1
# fit network
model = make_model()
history = model.fit(train_X, train_y, epochs=100, batch_size=100, validation_data=(test_X, test_y), verbose=2, shuffle=False)
#df1.columns = [x.replace("day_history_mv_avg.","") for x in df1.columns.tolist()]


from numpy import concatenate
import itertools 
import numpy as np
yhat = model.predict(test_X)

def first_predict(train_X):
    pred_x_last = train_X.tolist()
    pred_x_last_len = len(pred_x_last)
    pred_last = model.predict(np.array([pred_x_last[pred_x_last_len-1]]))
    last_predict = (y_max-y_min)*pred_last[0][0]+y_min
    return pred_last,last_predict

pred_last,last_predict = first_predict(train_X)
train_X1 = train_X
train_X1 = np.append(train_X,pred_last)


mv_avg = [5,10,15,20,30,40,50,60,120,150,200,300]
def make_mv_avg(train_X1):
    new_mv_avg = []
    for i in mv_avg:
        new_mv_avg.append(np.mean(train_X1[-i:]))
    return new_mv_avg
predict_list = []
predict_list.append(pred_last[0,0].tolist())
for i in range(0,10):
    if i==0:
        train_X1 = np.append(train_X1,pred_last)
    else:
        train_X1 = np.append(train_X1,pred_new)
    train_new_mv_avg = make_mv_avg(train_X1)
    train_new_history = train_X1[-29:]
    train_new_X1 = np.append(train_new_mv_avg,train_new_history)
    train_new_X = np.array([[train_new_X1.tolist()]])
    pred_new = model.predict(train_new_X)
    a1 = pred_new[0,0]
    predict_list.append(a1.tolist())

data_dict = {
        "test_Y":test_y[0:11].tolist(),
        "predict_Y": predict_list
        }


df_predict = pd.DataFrame(data_dict)
df_predict1 = df_predict.round(3)
print(df_predict1)




'''


test_X[0]



test_y1 = test_y[0:test_y_len].tolist()
p1 = yhat[0:test_y_len].tolist()
predict_y1 = list(itertools.chain(*p1))   
df_out = pd.DataFrame(data_dict)
df_out.round(2).to_csv("test.csv")


from sklearn.metrics import mean_squared_error
import numpy as np
predict_num = 60
print(mean_squared_error(test_y[0:40],yhat[0:40]))
print(mean_squared_error(test_y[0:40],yhat[0:40])/np.mean(test_y[0:40]))


pred_x_last = test_X.tolist()
pred_x_last_len = len(pred_x_last)
pred_last = model.predict(np.array([pred_x_last[pred_x_last_len-1]]))
last_predict = (y_max-y_min)*pred_last[0][0]+y_min
print(last_predict)
'''
'''
from davidyu_cfg import *
from functions.LinearReg import LinearReg
linear_reg = LinearReg()
test_yy = pd.DataFrame(test_y[0:40])
test_yy.columns = ["col_in"]
yhat_yy = pd.DataFrame(yhat[0:40])
yhat_yy.columns = ["col_in"]

print(linear_reg.single_linear_reg(test_yy,"col_in")[0])
print(linear_reg.single_linear_reg(yhat_yy,"col_in")[0])
'''






'''
train = values[:n_train_hours, :]
test = values[n_train_hours:, :]
# split into input and outputs
train_X, train_y = train[:, :-1], train[:, -1]
test_X, test_y = test[:, :-1], test[:, -1]
# reshape input to be 3D [samples, timesteps, features]
print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)

'''

'''
test_X = test_X.reshape((test_X.shape[0], test_X.shape[2]))
inv_yhat = concatenate((yhat, test_X[:, 1:]), axis=1)
inv_yhat = scaler.inverse_transform(inv_yhat)
inv_yhat = inv_yhat[:,0]
# invert scaling for actual
test_y = test_y.reshape((len(test_y), 1))
inv_y = concatenate((test_y, test_X[:, 1:]), axis=1)
inv_y = scaler.inverse_transform(inv_y)
inv_y = inv_y[:,0]
# calculate RMSE
rmse = sqrt(mean_squared_error(inv_y, inv_yhat))
print('Test RMSE: %.3f' % rmse)

'''


