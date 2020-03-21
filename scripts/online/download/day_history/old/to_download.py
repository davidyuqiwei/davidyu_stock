# -*- coding: UTF-8 -*-
"""
@ Author : Davidyu
@ Use: this script download the daily historical data
"""
from davidyu_cfg import *
from functions.connect_url import url_opener
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
## download data from yahoo
def download_data(stock_id,start_date,end_date):
    """
    input : - stock_id    stock_index
            - start date
            - end date
    output : - dataframe of the stock
             - stock index
    """
    import pandas_datareader as web
    df = web.get_data_yahoo(stock_id,start_date,end_date)
    #df = web.DataReader(stock_id, "yahoo", start_date, end_date)
    df = df.round(2)
    #df=pro.daily(ts_code=stock_id,start=start_date, end=end_date)
    stock_name = stock_id
    return df,stock_id
def run_download(stock_index,start_date,end_date,save_dir):
    '''
    run it and save to $save_dir
    the filename is i.e. 601398.csv
    '''
    import os
    stock_df,stock_name = download_data(stock_index,start_date,end_date)
    #-------------------- save data -------------------#
    file_name = stock_index[0:6]+'.csv'
    ## print(dir_day_history)
    save_file_name = os.path.join(save_dir,file_name)
    ###
    stock_df['stock_index'] = stock_index[0:6]
    stock_df.to_csv(save_file_name,index=1,header=None)
def make_stock_download_index(stock_index):
    if stock_index[0] == "6":
        stock_index1 = stock_index+".ss"
    elif stock_index[0] == "0":
        stock_index1 = stock_index+".sz"
    else:
        stock_index1 = stock_index
    return stock_index1
def main(stock_index): 
    #from dir_control.data_dir import dir_basic_info,dir_day_history,stk_index_list
    dir_day_history_insert = data_dict.get("day_history_insert")
    import os
    import pandas as pd
    import time
    import datetime
    #### ------------ para -------------------#
    ##  set start end date
    ##############################################
    ## comment it if not test
    ####
    #print(k)
    stock_index = make_stock_download_index(stock_index)
    try:
        run_download(stock_index,start_date,end_date,dir_day_history_insert)
        #print("sleep")
    except:
        print("the stock index cannot be download "+ str(stock_index))
        pass
    #f.close()
if __name__ =='__main__':
    import sys
    from davidyu_cfg import * #carefull about the seperator
    import datetime
    from functions.ForDownload import generate_stock_index,stk_index_list_gen
    start_date = datetime.datetime(1990,1,1)
    end_date = datetime.date.today()
    stock_index = sys.argv[1]
    main(stock_index)
    #copy_data_to_current_folder()
    #655 = 100
'''
def copy_data_to_current_folder():
    from dir_control.data_dir_v1 import data_dict
    dir_day_history_insert = data_dict.get("day_history_insert")
    #dir_day_history_insert = "./csv"
    ## combine all data
    os_str = "cat %s/*.csv > all.csv"%(dir_day_history_insert)
    print(os_str)
    os.system(os_str)
    # save to hive

'''



