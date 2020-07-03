from davidyu_cfg import *
import pandas as pd
from functions.DF_process import changeStockIndex
from functions.day_history.getDataFromSpark import *

df1 = pd.read_csv("/home/davidyu/stock/data/basic_info/stock_basic_info.csv")
df1 = changeStockIndex(df1,'code')
stk_diaoyan_list = df1['stock_index'].tolist()
stk_diaoyan_list = [x for x in stk_diaoyan_list if x[0:2] =='60' or x[0:2] =='00']
stk_diaoyan_tup = tuple(stk_diaoyan_list[0:20])

para = {
    'stock_tuple': stk_diaoyan_tup,
    'start_date': '',
    'end_date': '',
    "save_file_name":'history_part1.csv'
}
getSparkData = getDataFromSpark(para)
getSparkData.getDataFromSparkAll()





