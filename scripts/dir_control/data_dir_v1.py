'''
this script make the data dir in the main path
---  /home/davidyu/stock/data -- 
'''
import os
import pandas as pd
# main data dir
data_dir=["tmp",
        "day_history",
        "day_history_insert",
        "basic_info",
        "financial_report",
        "test",
        "news_report",
        "liutong_owner",
        "all_news"
        ]
main_data_dir="/home/davidyu/stock/data"
def create_dir_if_not_exist(dir_name):
	if not os.path.isdir(dir_name):
	    os.makedirs(dir_name)
# set sub dir
def dir_dict(data_dir):
    data_path=[]
    for i in data_dir:
        path1=os.path.join(main_data_dir,i)
        create_dir_if_not_exist(path1)
        data_path.append(path1)
    return data_path
data_all_path=dir_dict(data_dir)
data_dict=dict(zip(data_dir,data_all_path))
#print(data_dict.get("tmp"))


#print(dict(zip(data_dir,data_all_path)))

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
