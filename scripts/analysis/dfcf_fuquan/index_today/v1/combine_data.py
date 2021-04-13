import pandas as pd
df_base = pd.read_csv("./data/kdj_macd_hs300.csv")
file_list = ["turnover_rate_hs300.csv"]
df_list = []
for f1 in file_list:
    df1 = pd.read_csv("./data/"+f1)
    df_base = pd.merge(df_base,df1)
stock_name = pd.read_csv("/home/davidyu/stock/data/common/stock_name.csv")
df_base_out = pd.merge(df_base,stock_name)
df_base_out.insert(0,"stock_name", df_base_out.pop('stock_name'))
df_base_out.round(1).to_csv("./data/hs300_tech_index.csv",index=0)

