#ttps://blog.csdn.net/u012735708/article/details/82769711
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.utils import np_utils
import os 
data_dir = "/home/davidyu/stock/data/test/for_lstm"
df1 = pd.read_csv(os.path.join(data_dir,"601398.csv"))
#df1 = pd.read_csv(os.path.join(data_dir,"000917.csv"))
df1 = df1.dropna().round(2)
df1.columns = [x.replace("day_history_mv_avg.","") for x in df1.columns.tolist()]

df2 = df1.iloc[100:2000,[i for i in range(2,11)]]
values = df2.values


n_train_hours = 1700
train = values[:n_train_hours, :]
test = values[n_train_hours:, :]
# split into input and outputs
train_X, train_y = train[:, :-1], train[:, -1]
test_X, test_y = test[:, :-1], test[:, -1]
# reshape input to be 3D [samples, timesteps, features]
train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)


model = Sequential()
model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2])))
model.add(Dense(1))
model.compile(loss='mae', optimizer='adam')
# fit network
history = model.fit(train_X, train_y, epochs=50, batch_size=72, validation_data=(test_X, test_y), verbose=2, shuffle=False)


from numpy import concatenate

yhat = model.predict(test_X)

from sklearn.metrics import mean_squared_error
import numpy as np
predict_num = 60
print(mean_squared_error(test_y[0:40],yhat[0:40]))
print(mean_squared_error(test_y[0:40],yhat[0:40])/np.mean(test_y[0:40]))

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


