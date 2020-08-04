import pandas as pd
file_name = "/home/davidyu/stock/data/SH_index_RT/SH_index_amount_RT_2020-06-04.txt"
df1 = pd.read_csv(file_name,header=None)

df1.columns = ["stock_index","cum_amount","stock_time"]


df1["amount"] = df1["cum_amount"].diff(1)
df1["time"] = [x[11:16] for x in df1["stock_time"].values.tolist()]

df1["stock_date"] = [x[0:10] for x in df1["stock_time"].values.tolist()]

