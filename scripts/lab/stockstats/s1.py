import stockstats
import pandas as pd
stock = stockstats.StockDataFrame.retype(pd.read_csv('002032.csv'))

