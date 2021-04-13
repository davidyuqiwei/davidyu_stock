import pandas as pd
import json
from davidyu_cfg import *
from functions.check_dataframe_to_hive import *
from functions.data_dir import *
from functions.get_datetime import *
import sys
## 东方财富数据中心 
# json to DF
def load_the_json(filename,encode_in="utf-8"):
    #f = open(filename,encoding="latin1")
    f = open(filename,encoding=encode_in)
    a1 = f.read()
    raw_json = json.loads(a1)
    df_len = len(raw_json.keys())
    all_keys = list(raw_json.keys())
    return df_len,all_keys,raw_json


def json_to_df(file_in,cols,date_type,save_dir=None):
    df_len,all_keys,raw_json = load_the_json(file_in)
    json_string_raw = raw_json.get(all_keys[0])
    list_string = [x.split(",") for x in json_string_raw] 
    df1 = pd.DataFrame(list_string,columns = cols )
    df2 = df1
    now_date = get_the_datetime()[0]
    if date_type == "month":
        date_in = now_date.replace("_","-")[0:7]
    elif date_type == "day":
        date_in = now_date
    else:
        print("input date error")
        sys.exit(2)
    df2['stock_date'] = date_in
    save_name = file_in.split(".")[0]
    file_name = save_name+"_"+date_in+".csv"
    if save_dir==None:
        df2.to_csv(os.path.join('./',file_name),index=0)
    else:
        df2.to_csv(os.path.join(save_dir,file_name),index=0)


def json_to_df_raw(file_in,cols,date_type):
    df_len,all_keys,raw_json = load_the_json(file_in)
    json_string_raw = raw_json.get(all_keys[0])
    list_string = [x.split(",") for x in json_string_raw] 
    df1 = pd.DataFrame(list_string,columns = cols )
    df2 = df1
    now_date = get_the_datetime()[0]
    if date_type == "month":
        date_in = now_date.replace("_","-")[0:7]
    elif date_type == "day":
        date_in = now_date
    else:
        print("input date error")
        sys.exit(2)
    df2['stock_date'] = date_in
    return df2
def save_data(file_in,df2,date_type,save_dir=None):
    now_date = get_the_datetime()[0]
    if date_type == "month":
        date_in = now_date.replace("_","-")[0:7]
    elif date_type == "day":
        date_in = now_date
    else:
        print("input date error")
        sys.exit(2)
    save_name = file_in.split(".")[0]
    file_name = save_name+"_"+date_in+".csv"
    if save_dir==None:
        df2.to_csv(os.path.join('./',file_name),index=0)
    else:
        df2.to_csv(os.path.join(save_dir,file_name),index=0)
if __name__ == "__main__":
    current_dir = os.path.abspath(os.path.dirname(__file__))
    #print(current_dir)
    files = os.listdir(current_dir)
    print(files)
    file_in = [x for x in files if 'txt' in x][0]
    columns = ["id","stock_index","stock_name","liutong"]
    date_type = "day"
    json_to_df(file_in,columns,date_type)


#a1 = json_string_raw[0]
#print(a1)
'''
for i in range(0,df_len):
    json_string_raw = raw_json.get(all_keys[i])
    print(json_string_raw)

'''


