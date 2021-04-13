from davidyu_cfg import *
from functions.data_dir import *
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import *
import baostock as bs
# 获取指数(综合指数、规模指数、一级行业指数、二级行业指数、策略指数、成长指数、价值指数、主题指数)K线数据
# 综合指数，例如：sh.000001 上证指数，sz.399106 深证综指 等；
# 规模指数，例如：sh.000016 上证50，sh.000300 沪深300，sh.000905 中证500，sz.399001 深证成指等；
# 一级行业指数，例如：sh.000037 上证医药，sz.399433 国证交运 等；
# 二级行业指数，例如：sh.000952 300地产，sz.399951 300银行 等；
# 策略指数，例如：sh.000050 50等权，sh.000982 500等权 等；
# 成长指数，例如：sz.399376 小盘成长 等；
# 价值指数，例如：sh.000029 180价值 等；
# 主题指数，例如：sh.000015 红利指数，sh.000063 上证周期 等；

data_dir = data_dict.get("baostock")
lg = bs.login(user_id="anonymous", password="123456")

index_list = {"sh.000016":"上证50","sh.000300":"沪深300","sh.000905":"中证500"}

start_date='2005-01-01'
end_date='2021-02-22'
df2 = bs.query_history_k_data_plus("sh.000300","date,code,open,high,low,close,volume,amount,turn,tradestatus,pctChg,peTTM,psTTM,pcfNcfTTM,pbMRQ,isST",start_date='1998-01-01', end_date=end_date,frequency="d", adjustflag="1")
df3 = df2.get_data()
df3.to_csv("hs_300.csv",index=0)
#print(df3.head(10))
