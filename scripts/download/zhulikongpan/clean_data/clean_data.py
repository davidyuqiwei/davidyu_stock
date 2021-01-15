import pandas as pd
df1 = pd.read_csv("/home/davidyu/stock/data/history_data/zhulikongpan/zhulikongpan_2021-01-05_clean.csv",header=None)
column_names = ["stock_date","stock_index","stock_name","price","kongpan_ratio","kongpan_cn"]

df.columns = column_names
df1.sort_values("kongpan_ratio",ascending=False).head(30)

df1.to_csv("zhulikongpan_test.csv",index=0)














