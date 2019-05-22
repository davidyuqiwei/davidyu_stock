import tushare as ts
info = ts.get_stock_basics()
info.to_csv("/home/davidyu/data/basic_info/stock_basic_info.csv")

