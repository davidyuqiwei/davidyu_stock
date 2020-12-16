from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import *
from functions.update.cleanData import cleanData
import gc

data_file = os.path.join(tmp_data_dict.get("baostock"),"baostock.csv")
df1 = pd.read_csv(data_file)

df2 = df1[df1["date"]!="date"]
df2["code"] = df2["code"].str[3:]
#del df1
#gc.collect()
df2.round(2).to_csv(data_file,index=0)
