import tushare as ts


token="85c3e04d2d6861c6036fe74b68a644b0ef7d5f5cfd6ad28a453e26d8"
ts.set_token(token)

pro = ts.pro_api()

df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20180718')
