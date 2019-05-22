import os
import pandas as pd
# main data dir

main_data_dir="/home/davidyu/stock/data"
def create_dir_if_not_exist(dir_name):
	if not os.path.isdir(dir_name):
	    os.makedirs(dir_name)
# set sub dir
day_history="day_history"
dir_day_history=os.path.join(main_data_dir,day_history)
create_dir_if_not_exist(dir_day_history)

basic_info="basic_info"
dir_basic_info=os.path.join(main_data_dir,basic_info)
create_dir_if_not_exist(dir_basic_info)

financial_report="financial_report"
dir_financial_report=os.path.join(main_data_dir,financial_report)
create_dir_if_not_exist(dir_financial_report)


### ----------  stock list
basic_file_name="stock_basic_info.csv"
basic_file_in=os.path.join(dir_basic_info,basic_file_name)
stk_index_df=pd.read_csv(basic_file_in,header=None)
stk_index_list=stk_index_df[0].tolist()
