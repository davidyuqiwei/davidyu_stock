from davidyu_cfg import *
from functions.get_text_file import *
from functions.DFCF_json_to_df import *

columns = ["id","stock_index","stock_name","shiyinglv"]
date_type = "day"
df1 = json_to_df_raw("shiyinglv.txt",columns,date_type)
print(df1)
