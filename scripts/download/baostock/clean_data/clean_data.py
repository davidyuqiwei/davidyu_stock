from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import *
from functions.update.cleanData import cleanData
import gc

## combine the old data and the new data

now_date,now_date_time = get_the_datetime()
year = now_date[0:4]
file_year = year+".csv"

## read old and new dataframe
data_file = os.path.join(tmp_data_dict.get("baostock"),file_year)
history_data = os.path.join(data_path,"history_data","baostock","byyear",file_year)

df_new = pd.read_csv(data_file)
df_old = pd.read_csv(history_data,header=None)

df_old.columns = df_new.columns
## clean data
df1 = pd.concat([df_old,df_new])
df1 = df1.drop_duplicates()
df2 = df1[df1["date"]!="date"]
df2["code"] = df2["code"].str[3:]
df2.round(2).to_csv(history_data,index=0,header=None)
