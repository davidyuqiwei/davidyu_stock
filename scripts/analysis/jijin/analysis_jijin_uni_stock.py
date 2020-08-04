from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.combine_with_stock_basic_info import *
from functions.jijin.jijinAnalysis import jijinAnalysis
from functions.jijin.jijinAnalysis import *

jj = jijinAnalysis().loadData()

df1 = jj.DF
first_season = "2020-06-30"
last_season = "2020-03-31"

## 基金持有股票个数统计
jj_df1 = jj.jijinOwnCount(first_season) 
stock_list1 = jijinAna.jijinOwnStat(jj_df1,1,jj.df_select)
jj_df2 = jj.jijinOwnCount(last_season) 
stock_list2 = jijinAna.jijinOwnStat(jj_df2,1,jj.df_select)

#this_list = jj_df1["jijin_name"].tolist()
#last_list = jj_df2["jijin_name"].tolist()

stock_uni_list1 = stock_list1["stock_index"].unique().tolist()  
stock_uni_list2 = stock_list2["stock_index"].unique().tolist()  

ret = [ i for i in stock_uni_list1 if i not in stock_uni_list2 ]
print(ret)





