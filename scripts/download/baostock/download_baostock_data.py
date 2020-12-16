from davidyu_cfg import *
from functions.data_dir import *
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import *
import baostock as bs
data_dir = tmp_data_dict.get("baostock")

lg = bs.login(user_id="anonymous", password="123456")


stock_index=sys.argv[1]
#stock_index = "601398"
#stock_index = "601398"
if stock_index[0:2] == "60":
    stock_index_in = "sh."+stock_index
else:
    stock_index_in = "sz."+stock_index

df2 = bs.query_history_k_data_plus(stock_index_in,"date,code,open,high,low,close,volume,turn,amount,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST",start_date='2006-10-27', end_date='2020-08-11',frequency="d", adjustflag="1")
save_file = os.path.join(data_dir,stock_index+".csv")
df3 = df2.get_data()
df3.to_csv(save_file,index=0)

'''
参数名称    参数描述
date    交易所行情日期
code    证券代码
open    开盘价
high    最高价
low 最低价
close   收盘价
preclose    昨日收盘价
volume  成交量（累计 单位：股）
amount  成交额（单位：人民币元）
adjustflag  复权状态(1：后复权， 2：前复权，3：不复权）
turn    换手率
tradestatus 交易状态(1：正常交易 0：停牌）
pctChg  涨跌幅
peTTM   动态市盈率
pbMRQ   市净率
psTTM   市销率
pcfNcfTTM   市现率
isST    是否ST股，1是，0否))

'''
