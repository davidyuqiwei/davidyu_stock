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



def col_feature_in_model():
    col_close_in,col_volume_in = col_name_in(30)
    column_in = ['slopes'] + col_close_in + col_volume_in
    return column_in,col_close_in,col_volume_in
def model_raw_data_get(raw_data,column_in):
    model_data_raw = raw_data[column_in].reset_index()
    drop_col=[0]
    model_data_raw.drop(model_data_raw.columns[drop_col],
        axis=1, inplace=True)
    return model_data_raw


def clear_model_data(model_data1):
    ## get feature dataframe to clean it, 
    #so this case we drop close value equal to 0
    feature_DF = model_data1[col_close_in] 
    data_drop0 = model_data1.ix[~(feature_DF==0).all(axis=1), :]
    model_DF = data_drop0.dropna()
    return model_DF

#df_mm1 = df_fea1.ix[~(df_fea1==0).all(axis=1), :]

#df_mm1['label'] = df_mm1['slopes']

def DF_col_label(DF,col):
    DF[col][DF[col]>0]=1
    DF[col][DF[col]<=0]=0
    return DF

def row_norm(df1,col_in):
    df_x1 = df1[col_in]
    df2 = df_x1.mean(axis=1)
    df_x2 = df_x1.div(df2, axis='rows')
    return df_x2

raw_data = pd.read_csv("raw_sample_data.csv")

column_in,col_close_in,col_volume_in = col_feature_in_model()
model_raw_data = model_raw_data_get(raw_data,column_in)
## col_close_in,  choose the column in 
model_data1 = model_raw_data[['slopes']+col_close_in]

model1 = model_data1.dropna()
df_mm1 = clear_model_data(model_data1)

df_mm1['label'] = df_mm1['slopes']
df_mm1 =  DF_col_label(df_mm1,'label')


fea_nom1 = row_norm(df_mm1,col_close_in)
train_X = fea_nom1.values
train_Y = df_mm1.label.values
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV, train_test_split
import random
from sklearn.externals import joblib

scaler = StandardScaler()
x_std = scaler.fit_transform(train_X)
x_train, x_test, y_train, y_test = train_test_split(x_std, train_Y, test_size=.4)

clf = svm.SVC(gamma='auto')
#clf.fit(x_train, y_train)
clf.fit(x_train, y_train)
save_path_name = "svm_" + "train_model_raw.m"
joblib.dump(clf, save_path_name)
clf = joblib.load(save_path_name)

#1[]nd = [random.randint(0,30000) for _ in range(30)]
rand_ind = [random.randint(0,x_test.shape[0]) for _ in range(50)]
y_predict = clf.predict(x_test[rand_ind])
y_raw = y_test[rand_ind]
a1 = y_raw-y_predict
print(len(a1[a1==0])/50)




#clf.score(x_test[rand_ind],y_test[rand_ind])

'''
row_norm(df1,col_volume_in)
df2=df1.sum(axis=1)


df_X

model1 = model_data_raw.dropna()

start_index = df3.columns.tolist().index('close1')
feature_index = [x for x in range(start_index,df3.shape[1])]
index_in = [6]+feature_index
df_model_raw = df3.iloc[:,index_in]
df_model = df_model_raw.dropna()

df_X = df3.iloc[:,start_index:]
df_Y = df3['adj_close']


make_history_vol(df1,history_days)

'''

