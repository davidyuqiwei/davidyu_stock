from davidyu_cfg import *
from functions.connect_url import url_opener
from functions.ForDownload import generate_stock_index,stk_index_list_gen
from functions.data_dir import *
import time
from functions.make_dir import *

df1 = pd.read_csv('all.csv')
df1 = df1.drop_duplicates()

'||'.join([str(x) for x in df1['gainian'].tolist()]) 

def str_append(x):
    gainian_list = '||'.join([str(x) for x in x['gainian'].tolist()]) 
    x['gainian_list'] = gainian_list
    return x
def str_append_vv(x):
    gainian_list = '||'.join([str(x) for x in x['stock_index'].tolist()]) 
    x['list'] = gainian_list
    return x
df2 = df1.groupby('stock_name').apply(str_append).reset_index()

df3 = df2.groupby(['stock_name','stock_index'])['gainian'].count().reset_index()

df_ganian_list = df2[["stock_name","gainian_list"]].drop_duplicates()
df4 = pd.merge(df3,df_ganian_list,how='left',on = ["stock_name"])

df4.sort_values('gainian').to_csv('gainian_rank.csv',index=0,encoding="utf_8_sig")



## gainian stat
aa = df1.groupby('gainian')['stock_index','stock_name'].count().reset_index()
#aa = df1.groupby('gainian')['stock_index']
a2 = df1.groupby('gainian').apply(str_append_vv).reset_index()
a3 = a2[['gainian','list']].drop_duplicates()
df4 = pd.merge(aa,a3,how='left',on = ["gainian"])
df4.sort_values("stock_index").to_csv('gainian_stat.csv',index=0,encoding="utf_8_sig")

aa.sort_values("stock_index")

