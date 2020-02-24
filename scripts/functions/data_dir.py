'''
this script make the data dir in the main path
---  /home/davidyu/stock/data -- 
'''
import os
import pandas as pd
from davidyu_cfg import *
# main data dir
data_dir=["tmp",
        "day_history",
        "day_history_insert",
        "day_history_wangyi",
        "basic_info",
        "financial_report",
        "test",
        "news_report",
        "liutong_owner",
        "all_news",
        "DADAN",
        "DADAN_offline",
        "YeJiYuQi",
        "PDF",
        "tonghuashun",
        "SH_50index",
        "fenhong",
        "bankuai",
        "DFCF",
        "future_index",
        "pofa",
        "jijin",
        "dazongjiaoyi",
        "gainian",
        "owner",
        "shijinglv",
        "important_owner"
        ]
main_data_dir="/home/davidyu/stock/data"
def create_dir_if_not_exist(dir_name):
	if not os.path.isdir(dir_name):
	    os.makedirs(dir_name)
# set sub dir
## create the data dir and make it into dict
def dir_dict(data_dir):
    data_path=[]
    for i in data_dir:
        path1 = os.path.join(main_data_dir,i)
        create_dir_if_not_exist(path1)
        data_path.append(path1)
        path2 = os.path.join(download_path,i)
        path3 = os.path.join(analysis_path,i)
        create_dir_if_not_exist(path2)
        create_dir_if_not_exist(path3)
    return data_path
data_all_path = dir_dict(data_dir)
data_dict = dict(zip(data_dir,data_all_path))
#print(data_dict.get("DADAN_offline"))
def get_stock_index_all_list():
    dir_basic_info = data_dict.get("basic_info")
    basic_file_name="stock_basic_info.csv"
    basic_file_in=os.path.join(dir_basic_info,basic_file_name)
    #stk_index_df = pd.read_csv(basic_file_in,header=None)
    stk_index_df = pd.read_csv(basic_file_in)
    stk_index_list = stk_index_df['code'].tolist()
    stk_index_list = [str(x).zfill(6) for x in stk_index_list]
    return stk_index_list

stk_index_list = get_stock_index_all_list()


'''
dir_basic_info = data_dict.get("basic_info")
basic_file_name="stock_basic_info.csv"
basic_file_in=os.path.join(dir_basic_info,basic_file_name)
stk_index_df = pd.read_csv(basic_file_in,header=None)
stk_index_df = pd.read_csv(basic_file_in)
stk_index_list = stk_index_df['code'].tolist()
stk_index_list = [str(x).zfill(6) for x in stk_index_list]

'''


