import pandas as pd
import numpy as np
df1 = pd.read_csv("wy_kdj.csv")

df2 = df1[df1["stock_date"] != "stock_date"]
df2["kdjj"] = [ np.float(x) for x in df2["kdjj"].values]
df2["rsi_6"] = [ np.float(x) for x in df2["rsi_6"].values]





