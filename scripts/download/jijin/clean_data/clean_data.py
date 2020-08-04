from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.combine_with_stock_basic_info import *
from functions.jijin.jijinAnalysis import jijinAnalysis
from functions.jijin.jijinAnalysis import *

jj = jijinAnalysis().loadData()

df1 = jj.DF.drop_duplicates()
## clean data the colname is not duplicate
col1 = df1.columns.tolist()[0]
df2 = df1[df1[col1] != col1]

df2.to_csv(jj.data_fullname,index=0)



