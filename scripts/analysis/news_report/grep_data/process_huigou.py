import pandas as pd
df1 = pd.read_csv("huigou.csv",header=None,sep=" ")

df1.columns = ["stock_index","stock_date"]
df1 = df1.dropna()

df1["stock_index"] = [str(int(x)).zfill(6) for x in df1["stock_index"].values]
print(df1)
df2 = df1.groupby("stock_index").min()
print(df2.reset_index())
df3 = df2.reset_index()
df3.to_csv("huigou_out_data.csv",index=0)
