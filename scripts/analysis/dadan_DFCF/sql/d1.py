from davidyu_cfg import *
df2 = pd.read_csv("/home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/dadan_DFCF/sql/money_daily.csv")

df3 = df2[(df2["dt"]>="2020-06-01")&(df2["dt"]>="2020-06-31")]

df3["month"] = df3["dt"].str[0:8]+'01'

a1 = df3.groupby(["stock_index","month"]).sum().reset_index()

a2 = a1[(a1["zhongdan_liuru"]>0)&(a1["dadan_liuru"]>0)&(a1["month"]=="2020-12-01")]
#a2 = a1[(a1["zhongdan_liuru"]>0)&(a1["month"]=="2020-12-01")]
a2.sort_values("zhongdan_liuru")


