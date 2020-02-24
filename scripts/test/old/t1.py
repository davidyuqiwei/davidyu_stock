import pandas as pd
import json
from check_dataframe_to_hive import *

#df1 = pd.read_csv("test.txt",encoding="latin1",header=None)
#df1.columns.values[0]
def make_raw_dataframe():
    columns_in = ['bk_en','板块','公司家数','平均价格','涨跌额','涨跌幅', \
            '总成交量','总成交额','stock_index1','涨跌幅', \
            '当前价','涨跌额','领涨股']
    df1 = pd.DataFrame(columns = columns_in)
    return df1
def load_the_json(filename):
    f = open(filename,encoding="latin1")
    a1 = f.read()
    raw_json = json.loads(a1)  
    df_len = len(raw_json.keys())
    all_keys = list(raw_json.keys())
    return df_len,all_keys,raw_json
def loop_to_insert_data(df_len,all_keys,raw_json,df_raw):
    for i in range(0,df_len):
    	json_string_raw = raw_json.get(all_keys[i])
    	json_string_decode = json_string_raw.encode("latin1").decode("gbk").split(",")
    	df_raw.loc[i] = json_string_decode
    df_raw['stock_index'] =  [x[2:8] for x in df_raw['stock_index1'].tolist()]  
    return df_raw
#df1 = check(df1)
def main():
    df1 = make_raw_dataframe()
    df_len,all_keys,raw_json = load_the_json("test1.txt")
    df1 = loop_to_insert_data(df_len,all_keys,raw_json,df1)
    df1 = check(df1)
    return df1
if __name__ == "__main__":
    df1 = main()
    print(df1.head(10))
    print('all done')


#columns = ['bankuai_en','bankuai','gonsijiashu','pingjunjiage','zde',
#        'zdf','zxjl','zcje','stock_index','lzg_zdf','dqj','dqg_zde','lzg']


