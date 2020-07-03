from davidyu_cfg import *
data_dir = "/home/davidyu/stock/data/dadan_sina_offline"
file_name = "2020_07_02_154012.csv"
df1 = pd.read_csv(os.path.join(data_dir,file_name))

df1['zhuli_buy_money'] = df1['avg_price'] *df1['zhuli_buy_vol']
df1['zhuli_buy_money_jing'] = df1['avg_price'] *df1['zhuli_buy_vol'] -df1['avg_price'] *df1['zhuli_sale_vol']

df2 = df1.sort_values("zhuli_buy_money")
df2[["stock_name","stock_index","zhuli_buy_money"]]

df3 = df1.sort_values("zhuli_buy_money_jing")


df2 = df1.sort_values("zhuli_buy_money_jing",ascending=False)
df3 = df2[["stock_name","stock_index","avg_price","zhuli_buy_vol","zhuli_buy_money","zhuli_buy_money_jing"]]
print(df3.head(50))




