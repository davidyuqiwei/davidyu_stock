# -*- coding: UTF-8 -*-
"""
@ Author : Davidyu
@ Use: this script download the daily historical data
"""

## download data from yahoo
def download_data(stock_id,start_date,end_date):
    """
    input : - stock_id    stock_index
            - start date
            - end date
    output : - dataframe of the stock
             - stock index
    """
    import pandas_datareader.data as web
    df = web.DataReader(stock_id, "yahoo", start_date, end_date)
    df = df.round(2)
    #df=pro.daily(ts_code=stock_id,start=start_date, end=end_date)
    stock_name=stock_id
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

def main(input_index): 
    #from dir_control.data_dir import dir_basic_info,dir_day_history,stk_index_list
    from dir_control.data_dir_v1 import data_dict
    dir_day_history_insert = data_dict.get("day_history_insert")
    import os
    import pandas as pd
    import time
    import datetime
    #### ------------ para -------------------#
    ##  set start end date
    ##############################################
    #----------------------------------------------------#
    input_index = str(input_index)
    stk_index_list = stk_index_list_gen()
    totol_loop = len(stk_index_list)
    ## comment it if not test
    #dir_day_history_insert = "./csv/"
    i = stk_index_list[int(input_index)]
    ####
    '''
    f = open("process.log", 'a+')
    f.write(input_index+'\n')
    '''
    stock_index = generate_stock_index(i)
    #print(k)
    try:
        run_download(stock_index,start_date,end_date,dir_day_history_insert)
        #print("sleep")
    except:
        print("the stock index cannot be download "+ str(stock_index))
        pass
    #f.close()
def copy_data_to_current_folder():
    from dir_control.data_dir_v1 import data_dict
    dir_day_history_insert = data_dict.get("day_history_insert")
    #dir_day_history_insert = "./csv"
    ## combine all data
    os_str = "cat %s/*.csv > all.csv"%(dir_day_history_insert)
    print(os_str)
    os.system(os_str)
    # save to hive
if __name__ =='__main__':
    import tushare as ts
    import sys
    from davidyu_cfg import * #carefull about the seperator
    import datetime
    from functions.ForDownload import generate_stock_index,stk_index_list_gen
    start_date = datetime.datetime(1990,1,1)
    end_date = datetime.date.today()
    main(1254)
    #copy_data_to_current_folder()



