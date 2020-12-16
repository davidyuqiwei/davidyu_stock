import pandas as pd
from davidyu_cfg import *
from functions.colNames import setColname

data_dir = "day_history_wangyi"
file_in = os.path.join(tmp_data_dict.get(data_dir),data_dir+".csv")
#data_file = os.path.join(file_in,header=None)
df1 = pd.read_csv(file_in,header=None)
df1 = df1.drop_duplicates()
df1.columns = setColname().day_history_wangyi()

df2 = df1[df1["stock_date"]>="1997-01-01"]
df2.to_csv(file_in,index=0)
