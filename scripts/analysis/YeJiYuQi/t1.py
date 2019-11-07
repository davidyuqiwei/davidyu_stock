from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *



dir_yjyq = data_dict.get("YeJiYuQi")
now_date,now_date_time = get_the_datetime()

data_dir = os.path.join(dir_yjyq,now_date)
df1 = combine_csv_in_folder_raw(data_dir)

df1.columns = ["index","stock_index","stock_name","yeji_predict","yeji_abstract","profit_change_ratio",
        "profit_change","date"]


def filter_index(x):
    x1 = str(x).zfill(6)
    if x1[0:2] == '60' or x1[0:2] == '00':
        tag =1
    else:
        tag = 0
    return tag
df2 = df1[df1.stock_index.apply(filter_index)==1]


df2[df2.yeji_predict=="业绩大幅上升"]

