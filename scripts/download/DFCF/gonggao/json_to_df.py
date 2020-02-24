import pandas as pd
import json
from davidyu_cfg import *
from functions.check_dataframe_to_hive import *
from functions.data_dir import *
from functions.get_datetime import *

# 前十大股东占比

def make_raw_dataframe():
    columns_in = ['id','stock_index','stock_name','total_ratio']
    df1 = pd.DataFrame(columns = columns_in)
    return df1
def load_the_json(filename):
    #f = open(filename,encoding="latin1")
    f = open(filename)
    a1 = f.read()
    raw_json = json.loads(a1)
    df_len = len(raw_json.keys())
    all_keys = list(raw_json.keys())
    return df_len,all_keys,raw_json
def json_to_df(file_in):
    df_len,all_keys,raw_json = load_the_json(file_in)
    #print(raw_jsonjin_hetong.txt)
    json_string_raw = raw_json.get(all_keys[0])
    list_string = [x.split(",") for x in json_string_raw] 
    df1 = pd.DataFrame(list_string,columns = ['stock_index','stock_name','jijin_num','stock_date','status'])
    #df1['total_ratio'] = [float(x[3]) for x in list_string]
    #df2 = df1.sort_values("total_ratio")
    df2 = df1
    #print(df2)
    now_date = get_the_datetime()[0]
    date_month = now_date.replace("_","-")[0:7]
    df2['stock_date'] = date_month
    file_name = "test"+date_month+".csv"
    df2.to_csv(file_name,index=0)
if __name__ == "__main__":
    file_in = "jijin_hetong.txt"
    json_to_df(file_in)
#a1 = json_string_raw[0]
#print(a1)
'''
for i in range(0,df_len):
    json_string_raw = raw_json.get(all_keys[i])
    print(json_string_raw)

'''


