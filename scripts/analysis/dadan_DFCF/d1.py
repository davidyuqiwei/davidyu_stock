from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import *

now_date = "2020_06_19"
dir_dadan = data_dict.get("dadan_DFCF")
data_dir = dir_dadan

df1 = pd.read_csv(os.path.join(data_dir,"2020_08_03.csv"))

df1.columns = ["new_price","today_increase_ratio","stock_index","stock_name","zhuli_liuru",
        "chaodadan_liuru","chaodadan_liuru_ratio","dadan_liuru","dadan_liuru_ratio",
        "zhongdan_liuru","zhongdan_liuru_ratio","xiaodan_liuru","xiaodan_liuru_ratio","test1",
        "zhuli_liuru_ratio","test2","test3",
        "test4","stock_date"]


df1 = df1[df1['zhuli_liuru_ratio']!="-"]
df1['zhuli_liuru_ratio'] = df1['zhuli_liuru_ratio'].astype(float)
df1['zhuli_liuru'] = df1['zhuli_liuru'].astype(float)


df2 = df1[["stock_index","stock_name",'zhuli_liuru_ratio','zhuli_liuru']]
df2.sort_values("zhuli_liuru_ratio")
df2.sort_values("zhuli_liuru")

df1.columns = setColname().DADAN()




