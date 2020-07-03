import pandas as pd
from davidyu_cfg import *
from functions.colNames import *
data_file = "/home/davidyu/stock/data/dadan_sina_offline/2020_07_01_154011.csv"
df1 = pd.read_csv(data_file)

df1['zhuli_buy_money'] = df1['avg_price'] *df1['zhuli_buy_vol']
df1['zhuli_buy_money_jing'] = df1['avg_price'] *df1['zhuli_buy_vol'] -df1['avg_price'] *df1['zhuli_sale_vol']

df2 = df1.sort_values("zhuli_buy_money")
df2[["stock_name","stock_index","zhuli_buy_money"]]

df3 = df1.sort_values("zhuli_buy_money_jing")











