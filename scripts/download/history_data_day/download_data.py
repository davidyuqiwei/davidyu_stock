### this script download the daily historical data
import tushare as ts
import sys
sys.path.append("../..")  ## carefull about the seperator
#from dir_control.dir_setup import *
token="85c3e04d2d6861c6036fe74b68a644b0ef7d5f5cfd6ad28a453e26d8"
pro = ts.pro_api(token)

def download_data(stock_id,start_date,end_date):
    #df = ts.get_tick_data('600848',date='2018-12-12',src='tt')
    df=pro.daily(ts_code=stock_id,start=start_date, end=end_date)
    stock_name=stock_id
    return df,stock_id

def run_download(stock_index,start_date,end_date,save_dir):
    import os
    stock_df,stock_name=download_data(stock_index,start_date,end_date)
    #-------------------- save data -------------------#
    file_name=stock_index+'.csv'
    ## print(dir_day_history)
    save_file_name=os.path.join(save_dir,file_name)
    ###
    stock_df.to_csv(save_file_name,index=None)
def main():
    from dir_control.data_dir import dir_basic_info,dir_day_history,stk_index_list
    import os
    import pandas as pd
    import time
    #-------------- var to set ---------------#
    start_date="2013-01-01"
    end_date="2018-12-31"
    basic_file_name="stock_basic_info.csv"
    #-----------------------------------------#
    #----------------------------------------------------#
    for i in stk_index_list:
        if str(i)[0]=='3':
            pass
        elif len(str(i))<6:
            stock_index=str(i).zfill(6)+'.sz'
            run_download(stock_index,start_date,end_date,dir_day_history)
            print("sleep")
            time.sleep(5)
        elif str(i)[0]=='6':
            stock_index=str(i)+'.sh'
            run_download(stock_index,start_date,end_date,dir_day_history)
            print("sleep")
            time.sleep(5)
if __name__ =='__main__':
    main()



