import pandas as pd
import re
from davidyu_cfg import *
files = ["dfcf_bankuai.csv","dfcf_diyu.csv","dfcf_hangye.csv"]
df_all_list = []
for f1 in files:
    data_type= re.split('[._]',f1)[1]
    df1 = pd.read_csv(os.path.join(tmp_data_dict.get("dfcf_bankuai"),f1))
    df1["data_type"] = data_type
    df1.columns = ["x1","change_ratio","bankuai_no","bankuai_name","x2",
            "x3","x4","x5","x6","x7","x8","x9","x10","x11","x12","lead_stock_name","lead_stock_index","x15","dt","data_type"]
    df2 = df1[df1["x1"]!=0].drop_duplicates()
    df2.to_csv(os.path.join(tmp_data_dict.get("dfcf_bankuai"),f1),index=0)
    df_all_list.append(df2)

df_all = pd.concat(df_all_list)
df_all.to_csv(os.path.join(tmp_data_dict.get("dfcf_bankuai"),"dfcf_bankuai_all.csv"),index=0)



