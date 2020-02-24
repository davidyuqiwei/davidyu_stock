import pandas as pd
import sys
from davidyu_cfg import *
from functions.get_datetime import *  ## now_date,now_date_time = get_the_datetime()

def check_data_to_hive(df1):
    df_columns = df1.columns.tolist()
    df1['day'] = get_the_datetime()[0].replace("_","-")
    if 'stock_index' not in df_columns:
        print('error: no stock_index column in dataframe')
        sys.exit()
    elif 'stock_date' not in df_columns:
        df1['stock_date'] = df1['day']
    return df1


def check_data_to_hive_date(df1):
    df_columns = df1.columns.tolist()
    df1['day'] = get_the_datetime()[0].replace("_","-")
    if 'stock_date' not in df_columns:
        df1['stock_date'] = df1['day']
    return df1

