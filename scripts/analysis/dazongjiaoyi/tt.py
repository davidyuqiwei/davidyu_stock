from davidyu_cfg import *
from functions.check_dataframe_to_hive import *
from functions.data_dir import *


"""
SECUCODE 股票代码
SNAME   股票名称
TVAL 成交额
Zyl 折溢率
BUYERNAME 买方营业部
PRICE 成交价格
"""
data_dir = data_dict.get("dazongjiaoyi")

df1 = pd.read_csv(os.path.join(data_dir,"dazongjiaoyi_2020-02-20.csv"))

df2 = df1.groupby(["SECUCODE","SNAME"])['TVAL'].sum().reset_index()
#df2.sort_values("TVAL")
df2['SECUCODE'] = [str(x).zfill(6) for x in df2['SECUCODE'].tolist() ]
df2['SECUCODE'].to_csv("dazongjiaoyi_stock_list.csv",index=0)
#df1['price_diff'] = df1['PRICE']-df1['CPRICE']

# 折溢率 为正的购买
def zyl_postive(df1):
	df2 = df1[df1['Zyl']>0]
	df2['Zyl'] = df2['Zyl'] *100
	df3 = df2.groupby(["SNAME","SECUCODE","BUYERNAME","Zyl","PRICE"])['TVAL'].sum().reset_index()
	
	print(df3.sort_values("TVAL")[["SNAME","SECUCODE","BUYERNAME","Zyl","PRICE","TVAL"]].tail(30))








