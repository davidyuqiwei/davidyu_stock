import pandas as pd
import json
from davidyu_cfg import *
from functions.common.parseToDF import *

data_dir = tmp_data_dict.get("gainian")

df1 = pd.read_csv(os.path.join(data_dir,"gainian.csv"))

df2 = df1[df1["stock_date"] !="stock_date"].dropna()
del df2["id"]
del df2["stock_date"]
df3 = df2.drop_duplicates()

save_file = os.path.join(data_dir,"gainian_to_db.csv")
df3.to_csv(save_file,index=0)


