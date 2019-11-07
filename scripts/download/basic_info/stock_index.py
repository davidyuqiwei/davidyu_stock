import tushare as ts
info = ts.get_stock_basics()
info.to_csv("/home/davidyu/stock/data/basic_info/stock_basic_info.csv")
info.to_csv("all.csv")
