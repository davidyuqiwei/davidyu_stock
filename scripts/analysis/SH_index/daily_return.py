from davidyu_cfg import *
import pandas as pd
from functions.common.cleanData import *


data_file = "/home/davidyu/stock/data/test/SH_index_data.csv"

df1 = pd.read_csv(data_file)


df1 = cleanData.cleanColName(df1)
df1 = cleanData.setDt(df1)

df_out = pd.DataFrame()
df_out["sh_index_return"] = (df1.close.diff(1)/df1.close).values
df_out["dt"] = df1["dt"].values

df_out = df_out.dropna()
df_out.round(3).to_csv("sh_index_daily_return.csv",index=0)

