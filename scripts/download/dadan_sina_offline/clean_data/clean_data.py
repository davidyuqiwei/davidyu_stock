from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.combine_with_stock_basic_info import *

data_file = os.path.join(tmp_data_dict.get("dadan_sina_offline"),"dadan_sina.csv")
df1 = pd.read_csv(data_file)

## clean data the colname is not duplicate
col1 = df1.columns.tolist()[0]
df2 = df1[df1[col1] != col1].drop_duplicates(subset=["stock_index","stock_date"],keep='first')

df2.to_csv(data_file,index=0)



