import pandas as pd
from davidyu_cfg import *

data_dir = tmp_data_dict.get("all_owner")
raw_file = os.path.join(data_dir,"all_owner.csv")
df1 = pd.read_csv(raw_file)

df2 = df1[df1["stock_index"]!="stock_index"]
df2 = df2.drop_duplicates()
df2.to_csv(raw_file,index=0)



df3 = df2[df2["gudong_type"]=="QFII"]
df3.to_csv(os.path.join(data_dir,"QF.csv"),index=0)


df3 = df2[df2["gudong_type"]=="社保"]
df3.to_csv(os.path.join(data_dir,"shebao.csv"),index=0)

df3 = df2[df2["gudong_type"]=="基本养老基金"]
df3.to_csv(os.path.join(data_dir,"yanglaojijin.csv"),index=0)

df3 = df2[df2["gudong_type"]=="保险"]
df3.to_csv(os.path.join(data_dir,"baoxian.csv"),index=0)

df3 = df2[df2["gudong_type"]=="基金"]
df3.to_csv(os.path.join(data_dir,"jijin.csv"),index=0)
