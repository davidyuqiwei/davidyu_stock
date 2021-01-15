from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import *

data_dir = os.path.join(data_path,"history_data","zhulikongpan")
files = os.path.join(data_dir,"zhulikongpan_2021-01-09.csv")
files = os.path.join(data_dir,"zhulikongpan_2021-01-08.csv")

df1 = pd.read_csv(files,header=None)

df1.columns = ["stock_date","stock_index","stock_name","new_price","x1","x2",
        "x3","zhuli_1_price","zhuli_ratio","zhuli_status","zhuli_20_price","a1","a2","a3",
        "a4","a5","a6","a7","a8","a9","a10","a11"]


df2 = df1[df1["zhuli_status"]=='完全控盘']

