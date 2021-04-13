import pandas as pd
df1 = pd.read_csv("/home/davidyu/stock/data/shiny_data/python/macd/today_kdj_hs_300.csv")
stock_name = pd.read_csv("/home/davidyu/stock/data/shiny_data/data/stock_name.csv")
def load_index_300():
    df_300 = pd.read_csv("/home/davidyu/stock/data/common/index_300_raw.txt",header=None)
    index_300 = [str(x[0]).zfill(6) for x in df_300.values.tolist()]
    return index_300
index_300 = load_index_300()
df2 = df1[df1["stock_index"].isin(index_300)]

max_dt = df2.dt.max()
df3 = df2[df2["dt"]==max_dt]

df4 = df3[["stock_index","dt","macdh_5_34_5","macdh_mvavg5","rsi_6","kdjj","kdjk","wr_6","wr_10"]]
df4 = pd.merge(df4,stock_name,on=["stock_index"],how="left")

df4 = df4[["stock_index","stock_name","dt","macdh_5_34_5","macdh_mvavg5","rsi_6","kdjj","kdjk","wr_6","wr_10"]]
df4.to_csv("/home/davidyu/stock/data/shiny_data/data/hs300_tech_index.csv",index=0)


