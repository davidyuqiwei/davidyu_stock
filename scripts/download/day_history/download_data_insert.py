### this script download the daily historical data
import tushare as ts
import sys
sys.path.append("../..")  ## carefull about the seperator
#from dir_control.dir_setup import *

## download data from yahoo
def download_data(stock_id,start_date,end_date):
    import pandas_datareader.data as web
    df = web.DataReader(stock_id, "yahoo", start_date, end_date)
    df = df.round(2)
    #df=pro.daily(ts_code=stock_id,start=start_date, end=end_date)
    stock_name=stock_id
    return df,stock_id
def run_download(stock_index,start_date,end_date,save_dir):
    import os
    stock_df,stock_name = download_data(stock_index,start_date,end_date)
    #-------------------- save data -------------------#
    file_name=stock_index[0:6]+'.csv'
    ## print(dir_day_history)
    save_file_name=os.path.join(save_dir,file_name)
    ###
    stock_df['stock_index']=stock_index[0:6]
    stock_df.to_csv(save_file_name,index=1,header=None)
def main():
    sys.path.append("../..")
    #from dir_control.data_dir import dir_basic_info,dir_day_history,stk_index_list
    from dir_control.data_dir_v1 import data_dict,stk_index_list
    dir_day_history_insert=data_dict.get("day_history_insert")
    import os
    import pandas as pd
    import time
    import datetime
    #### ------------ para -------------------#
    start_date = datetime.datetime(2009,1,1)
    end_date = datetime.date.today()
    dir_basic_info = data_dict.get("basic_info")
    ##############################################
    #----------------------------------------------------#
    ## remove '300'
    stk_index_list=[x for x in stk_index_list if str(x).zfill(6)[0]!='3']
    for i in stk_index_list:
        try:
            if len(str(i))<6:  ## download for ShangZhen
                stock_index=str(i).zfill(6)+'.sz'
                run_download(stock_index,start_date,end_date,dir_day_history_insert)
                #print("sleep")
            elif str(i)[0]=='6':  ## download for ShangHai
                stock_index=str(i)+'.ss'
                run_download(stock_index,start_date,end_date,dir_day_history_insert)
                #print("sleep")
        except:
            stock_index = str(i).zfill(6)+'.sz'
            print(stock_index)
            pass
        time.sleep(2)
    ## combine all data
    os_str = "cat %s/*.csv > all.csv"%(dir_day_history_insert)
    print(os_str)
    os.system(os_str)
    # save to hive
if __name__ =='__main__':
    main()



