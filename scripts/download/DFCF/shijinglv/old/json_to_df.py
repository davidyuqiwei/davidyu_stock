import pandas as pd
import json
from davidyu_cfg import *
from functions.check_dataframe_to_hive import *
from functions.data_dir import *
from functions.get_datetime import *
from functions.DFCF_json_to_df import *
import sys
from functions.get_text_file import *

current_dir = os.path.abspath(os.path.dirname(__file__))
text_file,file_name_raw = get_text(current_dir)
columns = ["id","stock_index","stock_name","shijinglv"]
date_type = "day"
save_dir = "./"
df1 = json_to_df_raw(text_file,columns,date_type,save_dir)
print(df1.shape)
