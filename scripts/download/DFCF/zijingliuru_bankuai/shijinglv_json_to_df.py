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
current_dir = "./"
filename,file_name_raw = get_text(current_dir)

f = open(filename)
a1 = f.read()
s1 = a1.split("}")
i2 = s1[2][1:]+"}" 

i3 = json.loads(i2)
df1 = pd.DataFrame(i3,index=[0])


columns = ["id","stock_index","stock_name","shijinglv"]
date_type = "day"
#save_dir = data_dict.get("shijinglv")
save_dir = "./"
df1 = json_to_df_raw(text_file,columns,date_type)
print(df1.shape)
now_date,_ = get_the_datetime()
df1.to_csv(os.path.join(save_dir,"shijinglv_"+now_date+".csv"),index=0)

