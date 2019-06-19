import pandas as pd
from get_technical_indicators import *

test_file="/home/davidyu/stock/data/day_history_insert/601398.csv"

df1 = pd.read_csv(test_file,header=None)

df2 = df1.iloc[:,0:2]
df2.columns=['date','price']

df3 = get_technical_indicators(df2)
print(df3.head())



