import pandas as pd
import json
from davidyu_cfg import *
from functions.check_dataframe_to_hive import *
from functions.data_dir import *
from functions.get_datetime import *
from functions.DFCF_json_to_df import *
import sys

def create_envr():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    dir_dfcf = data_dict.get('DFCF')
    #print(current_dir)
    files = os.listdir(current_dir)
    #print(files)
    file_in = [x for x in files if 'txt' in x][0]
    dir_name = file_in.split(".")[0]
    save_dir = os.path.join(dir_dfcf,dir_name)
    create_dir_if_not_exist(save_dir)
    return file_in,save_dir
def json_to_df(filename):
    f = open(filename)
    a1 = f.read()
    raw_json = json.loads(a1)
    all_json = raw_json.get('pages')
    js1 = all_json[0]
    df1 = pd.DataFrame(js1,index=[0])
    for i in range(1,len(all_json)):
        js2 = all_json[i]
        df2 = pd.DataFrame(js2,index=[0])
        df1 = df1.append(df2)
    filedate = [ x[0:10] for x in df1.TDATE.tolist() ]
    df1['stock_date'] = filedate
    df1['day'] = filedate
    return df1,filedate[0]
if __name__ == "__main__":
    filein = sys.argv[1]
    df1,filedate = json_to_df(filein)
    #now_date,_ = get_the_datetime()
    save_name = "dazongjiaoyi_"+filedate+".csv"
    save_dir = data_dict.get("dazongjiaoyi")
    df1.to_csv(os.path.join(save_dir,save_name),index=0)
    df1.to_csv("today.csv",index=0)

    #df_len,all_keys,raw_json = load_the_json("dazongjiaoyi.txt")


