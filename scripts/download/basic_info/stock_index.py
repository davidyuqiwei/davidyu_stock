import tushare as ts
info = ts.get_stock_basics()
info.to_csv("all.csv")
