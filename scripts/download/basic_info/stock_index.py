import tushare as ts
pro = ts.pro_api('85c3e04d2d6861c6036fe74b68a644b0ef7d5f5cfd6ad28a453e26d8')


data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')


info = ts.get_stock_basics()
info.to_csv("stock_basic_info_nohead.csv",header=None)
info.to_csv("stock_basic_info.csv")



'''
code,代码
name,名称
industry,所属行业
area,地区
pe,市盈率
outstanding,流通股本(亿)
totals,总股本(亿)
totalAssets,总资产(万)
liquidAssets,流动资产
fixedAssets,固定资产
reserved,公积金
reservedPerShare,每股公积金
esp,每股收益
bvps,每股净资
pb,市净率
timeToMarket,上市日期
undp,未分利润
perundp, 每股未分配
rev,收入同比(%)
profit,利润同比(%)
gpr,毛利率(%)
npr,净利润率(%)
holders,股东人数

'''
