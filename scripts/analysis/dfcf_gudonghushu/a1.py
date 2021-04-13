import pandas as pd
df1= pd.read_csv("/home/davidyu/stock/data/tmp_data/dfcf_gudonghushu/dfcf_gudonghushu.csv")

df1 = df1[df1["dt"]!="dt"]
df2=df1[df1["dt"]>"2020-09-30T00"]

df3 = df2[["HolderNum","stock_index"]]
df3["HolderNum"] = [np.float(x) for x in df3["HolderNum"].values.tolist()]

df4=df3[df3["HolderNum"]>1000]
df4.sort_values("HolderNum")
