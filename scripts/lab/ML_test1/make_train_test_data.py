import pandas as pd
import os
from davidyu_cfg import *
from load_model_data import *
from functions.LinearReg import LinearReg
from functions.rolling_regression import *
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV, train_test_split
import random
from sklearn.externals import joblib
import numpy as np


def col_feature_in_model():
    col_close_in,col_volume_in = col_name_in(30)
    column_in = ['slopes'] + col_close_in + col_volume_in
    return column_in,col_close_in,col_volume_in

def clean_model_data(model_data1,col_close_in):
    ## get feature dataframe to clean it, 
    #so this case we drop close value equal to 0
    feature_DF = model_data1[col_close_in] 
    data_drop0 = model_data1.ix[~(feature_DF==0).all(axis=1), :]
    model_DF = data_drop0.dropna()
    return model_DF


def DF_col_label(DF,col):
    DF[col][DF[col]>0]=1
    DF[col][DF[col]<=0]=0
    return DF

def feature_norm(df1,col_in):
    df_x1 = df1[col_in]
    df2 = df_x1.mean(axis=1)
    df_x2 = df_x1.div(df2, axis='rows')
    return df_x2


def make_train_test_data(train_X,train_Y):
    scaler = StandardScaler()
    x_std = scaler.fit_transform(train_X)
    x_train, x_test, y_train, y_test = train_test_split(x_std, train_Y, test_size=.4)
    return x_train, x_test, y_train, y_test

def model_raw_data_get(raw_data,column_in):
    #raw data and get the column in 
    #drop not need column 
    model_data_raw = raw_data[column_in].reset_index()
    drop_col=[0]
    model_data_raw.drop(model_data_raw.columns[drop_col],
        axis=1, inplace=True)
    return model_data_raw

def make_model_data(raw_data,column_all,column_in_model):
    '''
    @param   column_all,   all the columns we are inters
    @param   column,   column in the final models
    '''
    model_data_raw = raw_data[column_in_model].reset_index()
    drop_col=[0]
    model_data_raw.drop(model_data_raw.columns[drop_col],
        axis=1, inplace=True)
    #column_in,col_close_in,col_volume_in = col_feature_in_model()
    ######################################################3
    ## col_close_in,  choose the column in 
    model_data1 = model_data_raw[column_in_model]
    return model_data1

def clean_data(model_data1,all_feature_col):
    ## clean model data
    model_data1 = model_data1.dropna()
    ## drop NA and 0 rows in the feature columns
    model_data2 = clean_model_data(model_data1,all_feature_col) 
    model_data2['label'] = model_data2['slopes']
    df_label =  DF_col_label(model_data2,'label')
    return df_label

def DF_norm_feature(df_label,feature_list_list):
    fea_nom1 = feature_norm(df_label,feature_list_list[0])
    df_feature_out = fea_nom1
    for i in range(1,len(feature_list_list)):
        fea_nom2 = feature_norm(df_label,feature_list_list[i])
        df_feature_out = pd.merge(df_feature_out,fea_nom2,left_index=True,right_index=True)
    return df_feature_out


def col_mv_avg(raw_data):
    mv_col_list = [x for x in raw_data.columns.tolist() if 'mv' in x]
    return mv_col_list

def flat_list_list(list_list):
    all_col = []
    for i in list_list:
        all_col += i
    return all_col

def make_minis_feature(DF,feature_col):
    a1 = feature_col
    tt = DF
    col_in = []
    for i in a1:
        for j in a1:
            if i !=j :
                col_name = i+'-'+j
                col_in.append(col_name)
                col_name_check = j+'-'+i
                if col_name_check not in col_in:
                    tt[col_name] = tt.loc[:,i] - tt.loc[:,j]     
    return tt

if __name__=='__main__':
    raw_data = pd.read_csv("raw_sample_data.csv")
    ### column in 
    column_in,col_close_in,col_volume_in = col_feature_in_model()
    mv_col_list = col_mv_avg(raw_data) ## moving average list
    all_col1 = [['slopes'],col_close_in,mv_col_list]  # all list: list of list
    feature_list_list = [col_close_in,mv_col_list]
    all_col = flat_list_list(all_col1) ## flat all list
    feature_col = flat_list_list(feature_list_list)
    model_data1 = make_model_data(raw_data,column_in,all_col)
    ###############################################################3
    df_label = clean_data(model_data1,all_col)
    test1 = make_minis_feature(df_label,feature_col)
    test_col = test1.columns.tolist()
    test_col_in = [x for x in test_col if '-' in x]
    #feature_DF = DF_norm_feature(df_label,feature_list_list)  
    feature_DF = df_label[test_col_in]
    feature_DF[feature_DF>0]=1
    feature_DF[feature_DF<=0]=0
    #fea_nom1,df_label = clean_data(model_data1,col_close_in)
    train_X = feature_DF.values
    train_Y = df_label.label.values
    # ----- train ------#
    #scaler = StandardScaler()
    #x_std = scaler.fit_transform(train_X)
    x_train, x_test, y_train, y_test = train_test_split(train_X, train_Y, test_size=.4)
    ##
    import pickle
    output_test = open('test_data.pkl', 'wb')
    data1 = {
        'x_test':x_test,
        'y_test':y_test
        }
    #output = open('data.pkl', 'wb')
    pickle.dump(data1, output_test)
    
    output_train = open('train_data.pkl', 'wb')
    data1 = {
        'x_train':x_train,
        'y_train':y_train
        }
    #output = open('data.pkl', 'wb')
    pickle.dump(data1, output_train)

    '''
    model_fit = []
    for i in range(100):
        rand_ind = [random.randint(0,x_test.shape[0]) for _ in range(50)]
        y_predict = clf.predict(x_test[rand_ind])
        y_raw = y_test[rand_ind]
        a1 = y_raw-y_predict
        fit_ratio = len(a1[a1==0])/50
        #print(fit_ratio)
        model_fit.append(fit_ratio)
    print(np.mean(model_fit))

    '''
