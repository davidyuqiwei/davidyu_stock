import sys
import pandas as pd
from davidyu_cfg import *
from functions.connect_url import url_opener
from functions.get_datetime import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
dir_dadan = data_dict.get("DADAN_offline")
now_date,now_date_time = get_the_datetime()

now_date="2020_01_10"
data_dir = os.path.join(dir_dadan,now_date)
print(data_path)

os.system("find %s | xargs cat  *.csv > %s/all.csv" %(data_dir,dir_dadan))
os.system("sed -e '/0,1,2/d'  %s/all.csv  > %s/all_v1.csv" %(dir_dadan,dir_dadan))

df1 = pd.read_csv(os.path.join(dir_dadan,"all_v1.csv"))
df1 = df1.drop_duplicates()
df1.to_csv(os.path.join(dir_dadan,now_date+".csv"),index=0)

os.system("rm -rf %s/all.csv %s/all_v1.csv" %(dir_dadan,dir_dadan))

