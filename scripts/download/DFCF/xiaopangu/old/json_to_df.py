import pandas as pd
import json
from davidyu_cfg import *
from functions.check_dataframe_to_hive import *
from functions.data_dir import *
from functions.get_datetime import *
from functions.DFCF_json_to_df import *
import sys
## 东方财富数据中心 
# json to DF




if __name__ == "__main__":
    current_dir = os.path.abspath(os.path.dirname(__file__))
    dir_dfcf = data_dict.get('DFCF')
    #print(current_dir)
    files = os.listdir(current_dir)
    #print(files)
    file_in = [x for x in files if 'txt' in x][0]
    dir_name = file_in.split(".")[0]
    save_dir = os.path.join(dir_dfcf,dir_name)
    create_dir_if_not_exist(save_dir)
    columns = ["id","stock_index","stock_name","liutong"]
    date_type = "day"
    json_to_df(file_in,columns,date_type,save_dir)
    print("python run finish")

#a1 = json_string_raw[0]
#print(a1)
'''
for i in range(0,df_len):
    json_string_raw = raw_json.get(all_keys[i])
    print(json_string_raw)

'''


