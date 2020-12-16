from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import *
from functions.update.cleanData import cleanData


data_file = os.path.join(tmp_data_dict.get("YeJiYuQi"),"YeJiYuQi.csv")
df1 = pd.read_csv(data_file)
df1.columns = setColname().yejiyuqi()
df1 = df1[df1["stock_date"]!="7"] 
del df1["index"]
df2 = df1.drop_duplicates()
df2 = cleanData.columnToFloat(df2,["profit_change_ratio"])
df2.rename(columns={"date":"stock_date"},inplace = True)
df2.to_csv(data_file,index=0,header=None)
