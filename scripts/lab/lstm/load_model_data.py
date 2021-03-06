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

if __name__ == "__main__":
    data_dir = "/home/davidyu/stock/data/test/for_lstm"
    file_name = "SH_index.csv"
    df1 = read_mv_avg_data_clean(data_dir,file_name)
    history_days = 30
    df1 = make_history_price(df1,history_days)
    train_nums = 4000
    y_start = 2 
    train_X,train_y,test_X,test_y,y_min,y_max = make_train_test_data(df1,train_nums,y_start)



