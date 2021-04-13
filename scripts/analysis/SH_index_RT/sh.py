import pandas as pd
file_name = "/home/davidyu/stock/data/history_data/sh_index_rt/SH_index_amount_RT_2020_all.txt"
df1 = pd.read_csv(file_name,header=None)

df1.columns = ["price","cum_amount","stock_date_time"]
df1 = df1.drop_duplicates()
df1["stock_date"] = [x[0:10] for x in df1["stock_date_time"].values.tolist()]
df1["hr"] = [x[11:13] for x in df1["stock_date_time"].values.tolist()]
df1["time"] = [x[11:16] for x in df1["stock_date_time"].values.tolist()]
def clean_rt_data(df1):
    #df1 = df1.sort_values("time")
	#df1["amount"] = df1["cum_amount"].diff(1)
	#df1["time"] = [x[11:16] for x in df1["stock_date_time"].values.tolist()]
	#df1["hr"] = [x[11:13] for x in df1["stock_date_time"].values.tolist()]
    df1 = df1.sort_values("time")
	df1["amount"] = df1["cum_amount"].diff(1)
	df2 = df1[(df1["time"]>="09:30")&(df1["time"]<="15:00")]
	df3 = df2[(df2["time"]<="11:30")|(df2["time"]>="13:00")]
    return df3

df2 = df1.groupby("stock_date").apply(clean_rt_data)
df3 = df2.reset_index(drop=True)


def price_vol(df2):
    try:
        group = pd.cut(df2["price"].values,10)
        df2["group"] = group
        df_out = df2.groupby("group")["amount"].sum()
        df_out = df_out.reset_index()
    except:
        df_out = pd.DataFrame()
        df_out["group"] = 'no'
        df_out["amount"] = -999
    return df_out
df3 = df2.reset_index(drop=True)
df4 = df3.groupby("stock_date").apply(price_vol)
df5 = df4.reset_index()

df5.to_excel("sh_index_rt_vol_price.xlsx",index=0)
