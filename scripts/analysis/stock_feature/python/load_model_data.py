#https://blog.csdn.net/u012735708/article/details/82769711
'''
@update time 2020.4.3
@desc: make the feature of stock daily data
'''
import pandas as pd
import os 
from davidyu_cfg import *
from functions.day_history.load_model_data import *
from functions.stock_feature.make_history_shift_data import *
from functions.stock_feature.read_csv_data import *



def normalize_DF(df):
    ## normalize the dataframe
    #  (x-min_x)/(max_x-min_x)
    df_models_raw = df
    df_norm = (df_models_raw-df_models_raw.min())/(df_models_raw.max()-df_models_raw.min())
    return df_norm


def close_volume_change(df1,start_index,row_num):
    '''
    @desc:  difference of every of two feature column

    @para df1:  the dataframe has features of adj_close and volume
    @para start_index : the start index put in the model, for column  [y,x1,x2,x3]
    @para row_num,the rows to process dataframe
    '''
    df_models_raw = df1.iloc[:,start_index:]  
    feature_col_name = df_models_raw.columns.tolist()
    feature_column_num = df_models_raw.shape[1]  ## the colums of feather
    new_fea_name = []
    fea_value_list = []
    for i in range(0,feature_column_num):
        for j in range(0,feature_column_num):
            if feature_col_name[i] != feature_col_name[j]:
	            if ('close' in feature_col_name[i] and 'close' in feature_col_name[j]) or \
	                    ('volume' in feature_col_name[i] and 'volume' in feature_col_name[j]):
	                fea_name = feature_col_name[i] + "||" + feature_col_name[j]
	                new_fea_name.append(fea_name)
	                fea_value = df_models_raw.iloc[row_num,i] - df_models_raw.iloc[row_num,j]
	                fea_value_list.append(fea_value)
            else:
                pass
    return fea_value_list,new_fea_name


def loop_rows_close_volume_change(df1,start_index):
    df_models_raw = df1.iloc[:,start_index:]
    feature_rows = df_models_raw.shape[0]
    rows = df_models_raw.shape[0]
    feature_value_list_all = []
    for i in range(0,rows):
        a1,feature_name = close_volume_change(df1,start_index,i)
        a1 = [df3.adj_close[i],df3.high[i],df3.low[i]] + a1
        feature_value_list_all.append(a1)
    return feature_value_list_all,feature_name 


def test():
    ## normalized the dataframe   
    df_models = normalize_DF(df_models_raw)
    df_X = df_models.iloc[start_from_num:df_models.shape[0],[i for i in range(feature_start_index,df_models.shape[1])]]
    df_Y = df_models.iloc[start_from_num:df_models.shape[0],0]
    all_x_values = df_X.values
    all_y_values = df_Y.values
    train_X = all_x_values[:train_nums, :]  # e.g. train_nums = 1000 , train data is the first 1000 data
    train_y = all_y_values[:train_nums]
    test_X = all_x_values[train_nums:, :] # test data   after 1000 data
    test_y = all_y_values[train_nums:]
    train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
    test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
    y_min = df_models_raw.min()[0]
    y_max = df_models_raw.max()[0]
    return train_X,train_y,test_X,test_y,y_min,y_max

def tomorrow_change(df1):
    df2 = df1.copy(deep=False)
    df2['close_diff'] = df2['adj_close'].diff()
    df_models_raw = df1.iloc[:,2:]
    df_feature_columns = df_models_raw.columns[1:].tolist()   
    df_feature_raw = df2[df_feature_columns]
    
    ij_combine_list = []
    for i in range(0,len(df_feature_columns)):
        for j in range(0,len(df_feature_columns)):
            if i==j or df_feature_columns[i] == 'volume' or df_feature_columns[j]=='volume':
                pass
            else:
                ij_combine = [i,j]
                ij_combine.sort()
                ij_str = ';'.join([df_feature_columns[i],df_feature_columns[j]])
                if ij_str in ij_combine_list:
                    pass
                else:
                    df_feature_raw[ij_str] = df_feature_raw[df_feature_columns[i]] - df_feature_raw[df_feature_columns[j]]
                    ij_combine_list.append(ij_str)
            #if i==j or df_feature_columns[i] == 'volume' or df_feature_columns[j]=='volume' or ij_str in ij_combine_list:
            #    pass
            #else:


if __name__ == "__main__":
    data_dir = "/home/davidyu/stock/data/tmp_data/stock_feature"
    file_name = "SH_index.csv"
    start_index = 2
    history_days = 30

    df1 = clean_data().read_csv_clean(data_dir,file_name).clean_colname().sort_df("stock_date")
    tt = make_history_shift_data()
    df2 = tt.make_history_price(df1,history_days)
    df3 = tt.make_history_volume(df2,history_days)
    #print(df2.head(50))
    a1,feature_name = loop_rows_close_volume_change(df3,start_index)
    df_out = pd.DataFrame(a1)
    df_out.columns = ['adj_close','high','low']+feature_name
    df_out['close_change'] = df_out['adj_close'].diff(1).shift(-1)
    df_out['high_change'] = df_out['high'].diff(1).shift(-1)
    df_out['low_change'] = df_out['low'].diff(1).shift(-1)
    
    df_out = df_out.dropna()
    
    #df_out[df_out>0] = 1
    #df_out[df_out<=0] = 0
    file_name = os.path.join(tmp_data_path,"stock_feature","stock_feature1.csv")
    #df_out.to_csv(file_name,index=0)

























    '''
    df_out1 = df_out.tail(4000)
    df_feature = df_out1.iloc[:,3:3446].values
    df_y = df_out1.iloc[:,3447].values
    
    X_train, X_test, y_train, y_test  = train_test_split(df_feature,df_y, test_size=0.33, random_state=42)


    import xgboost as xgb
    import numpy as np
    from sklearn.model_selection import train_test_split


    #data = np.random.rand(5, 10)  # 5 entities, each contains 10 features
    #label = np.random.randint(2, size=5)  # binary target
    dtrain = xgb.DMatrix(X_train, label=y_train)
    dtest = xgb.DMatrix(X_test)
	params={'booster':'gbtree',
	        'objective': 'binary:logistic',
	        'eval_metric': 'auc',
	        'max_depth':7,
	        'lambda':15,
	        'subsample':0.75,
	        'colsample_bytree':0.75,
	        'min_child_weight':1,
	        'eta': 0.025,
	        'seed':0,
	        'nthread':8,
	        'silent':1,
	        'gamma':0.15,
	        'learning_rate' : 0.05}
    watchlist = [(dtrain,'train')]
    bst = xgb.train(params,dtrain,num_boost_round=100,evals=watchlist)
    ypred = bst.predict(dtest)

    '''







    '''
    history_days = 30
    df1 = make_history_price(df1,history_days)
    df1 = make_history_vol(df1,history_days)
    train_nums = 4000
    y_start = 2 
    train_X,train_y,test_X,test_y,y_min,y_max = make_train_test_data(df1,train_nums,y_start)

    '''


