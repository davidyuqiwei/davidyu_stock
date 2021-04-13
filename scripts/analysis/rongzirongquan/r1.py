import sys
from davidyu_cfg import *
from functions.data_dir import *
from functions.get_datetime import *
from functions.common.save_DataFrame import save_df_date
from functions.common.TimeMake import *
import re

df1 = pd.read_csv("/home/davidyu/stock/data/rongzirongquan/rongzirongquan_2020-12-09_4.csv")
df1.columns = ['DATE', 'MARKET', 'SCODE', 'SECNAME', 'RZYE', 'RQYL', 'RZRQYE', 'RQYE', 'RQMCL', 'RZRQYECZ', 
'RZMRE', 'SZ', 'RZYEZB', 'RZMRE3D', 'RZMRE5D', 'RZMRE10D', 'RZCHE', 'RZCHE3D', 'RZCHE5D', 'RZCHE10D', 'RZJME', 
'RZJME3D', 'RZJME5D', 'RZJME10D', 'RQMCL3D', 'RQMCL5D', 'RQMCL10D', 'RQCHL', 'RQCHL3D', 'RQCHL5D', 'RQCHL10D', 
'RQJMG', 'RQJMG3D', 'RQJMG5D', 'RQJMG10D', 'SPJ', 'ZDF', 'RCHANGE3DCP', 'RCHANGE5DCP', 'RCHANGE10DCP', 'KCB', 'TRADE_MARKET_CODE', 'TRADE_MARKET']

df1.to_csv("rzrq_sample.csv",index=0)

