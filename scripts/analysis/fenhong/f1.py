from davidyu_cfg import *
from functions.run_combine_all_csv import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist

df1 = combine_csv_in_folder_raw("/home/davidyu/stock/data/fenhong")
df2 = df1[df1['除权除息日'] >="2019-12-31"]

#df2['派息']/(df2['最新价']*100)

x1 = [float(x) if x!='停牌' else 999 for x in df2['最新价'].tolist()]
x2 = [float(x) if x!='--' else -1 for x in df2['派息'].tolist()]

df2['paixi'] = x2
df2['price'] = x1
df2['paixi_ratio'] = df2['paixi']/df2['price']

df3 = df2[["股票代码","股票简称","paixi_ratio"]]


high_paixi_num = 30

df_sammple = df3.sort_values("paixi_ratio").tail(50)
high_fenhong_stock_list1 = df_sammple['股票代码']
high_fenhong_stock_list = [str(x).zfill(6) for x in high_fenhong_stock_list1]

#df2[df2['股票代码']==601216][["除权除息日","股权登记日"]]
###########################################################
###########################################################
#df_sum  = df1.groupby('股票代码').sum()
#df_sum.sort_values('paixi',ascending=False)

from davidyu_cfg import *
import pandas as pd
from functions.DF_process import changeStockIndex
from functions.day_history.getDataFromSpark import *

stk_tuple = tuple(high_fenhong_stock_list)
para = {
    'stock_tuple': stk_tuple,
    'start_date': '',
    'end_date': '',
    "save_file_name":'fenhong_data.csv'
}

getSparkData = getDataFromSpark(para)
getSparkData.getDataFromSparkAll()



#df3 = df2.sort_values('paixi',ascending=False)  


