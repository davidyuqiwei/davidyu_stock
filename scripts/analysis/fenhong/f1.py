from davidyu_cfg import *
from functions.run_combine_all_csv import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist

df1 = combine_csv_in_folder_raw("/home/davidyu/stock/data/fenhong")
df2=df1[df1['除权除息日'] >="2018-12-31"]
df2['派息']/(df2['最新价']*100)

x1 = [float(x) if x!='停牌' else 999 for x in df1['最新价'].tolist()]
x2 = [float(x) if x!='--' else -1 for x in df1['派息'].tolist()]

df1['paixi'] = x2
df1['price'] = x1

df1['paixi_ratio'] = df1['paixi']/df1['price']

df_sum  = df1.groupby('股票代码').sum()
df_sum.sort_values('paixi',ascending=False)


df3 = df2.sort_values('paixi',ascending=False)  

df3[['股票代码','股票简称','最新价','派息']]

