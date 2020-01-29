from davidyu_cfg import *
import pandas as pd
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.run_combine_all_csv import *


dir_dadan = data_dict.get("DADAN")
df1 = combine_csv_in_folder(dir_dadan)
#df1.to_csv("all.csv",index=0)
df1.columns = ["stock_index","stock_name", \
            "trade_time","price","trade_num","trade_shou", \
            "status","price_change_rate","price_change_ratio","look","stock_date"]
df1['stock_index'] = [ str(x).zfill(6) for x in df1.stock_index.tolist()]
df1['day'] = [x.replace("_","-") for x in df1.stock_date.tolist()]
tmp_dir = data_dict.get("tmp")
df1.to_csv(os.path.join(tmp_dir,"DADAN_sample.csv"),index=0)

