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

def create_envr():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    dir_dfcf = data_dict.get('DFCF')
    #print(current_dir)
    files = os.listdir(current_dir)
    #print(files)
    file_in = [x for x in files if 'txt' in x][0]
    #print(file_in)
    dir_name = file_in.split(".")[0]
    save_dir = os.path.join(dir_dfcf,dir_name)
    create_dir_if_not_exist(save_dir)
    return file_in,save_dir

if __name__ == "__main__":
    columns = ["id","stock_index","stock_name","gainian"]
    date_type = "day"
    file_in,save_dir = create_envr()
    save_dir = data_dict.get("gainian")
    df1 = json_to_df_raw(file_in,columns,date_type,save_dir)
    df2 = df1
    now_date = get_the_datetime()[0]
    #print(df2.tail())
    save_name = df2['gainian'].tolist()[1]+".csv"
    #df2.to_csv("gainian.csv",index=0)
    df2.to_csv(os.path.join(save_dir,save_name),index=0)
    #save_data(file_in,df2,date_type,save_dir)
    print("python run finish")


#a1 = json_string_raw[0]
#print(a1)
'''
for i in range(0,df_len):
    json_string_raw = raw_json.get(all_keys[i])
    print(json_string_raw)

'''


