from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.colNames import setColname
data_file = os.path.join(tmp_data_dict.get("JiGouDiaoYan"),"jigoudiaoyan.csv")

df1 = pd.read_csv(data_file,error_bad_lines=False)
cols = setColname().jigoudiaoyan()
df1.columns = cols


df1.rename(columns={"date":"stock_date"},inplace=True)
df2 = df1[df1[df1.columns[3]] != df1.columns[3]]
df2 = df2[df2["ChangePercent"]!="stock_date"]
df2.to_csv(data_file,index=0,header=None)

