from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import *

df1 = pd.read_csv("owner_change.csv",header=None)

df1.columns = ["stock_index","stock_name","owner_name","change_type","notice_date","change_num"]

df2 = df1.drop_duplicates()
df3 = df2.sort_values("change_num")
print(df3.tail(30))

