from davidyu_cfg import *
from functions.pyspark_functions import *
from functions.baostock.stock_return import *
from functions.common.loadModule.load_module_kdj import *

sql1 = """
    select close,open,high,low,stock_date,lpad(stock_index,6,'0') as stock_index
    from 
    stock_dev.dfcf_fuquan_byyear
    where (substr(lpad(stock_index,6,'0'),1,2)='60' or substr(lpad(stock_index,6,'0'),1,2)='00')
    and year >=2016 and lpad(stock_index,6,'0') in 
    (select stock_index from stock_dev.sample_stock_index)
"""


def kdj_x(x):
    stock = DF_to_StockDataFrame(x)
    ss,tt = stock_kdj(stock)
    #print(ss)
    return ss


df1 = spark.sql(sql1)
df2 = df1.toPandas()

df2["close"] = [ np.float(x) for x in df2["close"].values.tolist() ]
df2["low"] = [ np.float(x) for x in df2["low"].values.tolist() ]
df2["high"] = [ np.float(x) for x in df2["high"].values.tolist() ]
df2["open"] = [ np.float(x) for x in df2["open"].values.tolist() ]

df3 = df2.groupby("stock_index").apply(lambda x: kdj_x(x))

df4 = df3.reset_index(drop=True)
df4 = df4.dropna().round(3).drop_duplicates()
#df4[df4["stock_index"]=='601398']

df_h1 = spark.createDataFrame(df4)
df_h1.write.format("orc").mode("overwrite").saveAsTable("stock_dw.dfcf_fuquan_kdj")






