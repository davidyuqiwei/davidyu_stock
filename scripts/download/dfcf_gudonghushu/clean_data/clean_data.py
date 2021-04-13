from davidyu_cfg import *
from functions.common.parseToDF import *
from functions.get_datetime import *
from functions.common.dfProcess import dfProcess
from functions.data_dir import create_dir_if_not_exist

df1 = pd.read_csv(os.path.join(tmp_data_dict.get("dfcf_gudonghushu"),"dfcf_gudonghushu.csv"))

df2 = df1[df1["stock_index"]!="stock_index"].drop_duplicates()
df2["EndDate"] = [x[0:10] for x in df2["EndDate"].values.tolist()]
df2["dt"] = df2["EndDate"]
save_dir = os.path.join(data_path,"history_data","dfcf_gudonghushu")

save_file = os.path.join(save_dir,"dfcf_gudonghushu.csv")
df2.to_csv(save_file,mode='a',index=None)


