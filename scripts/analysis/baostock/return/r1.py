from davidyu_cfg import *
from functions.pyspark_functions import *
from functions.baostock.stock_return import *

sql1 = """
    select close,dt,lpad(stock_index_raw,6,'0') as stock_index
    from 
    stock_dev.baostock_byyear
    where (substr(lpad(stock_index_raw,6,'0'),1,2)='60' or substr(lpad(stock_index_raw,6,'0'),1,2)='00')
    and year >=2020
"""

df1 = spark.sql(sql1)
df2 = df1.toPandas()
df2["close"] = [ np.float(x) for x in df2["close"].values.tolist() ]
df3 = df2.groupby("stock_index").apply(lambda x: stock_return(x,"close"))

df4 = df3.reset_index(drop=True)
df4 = df4.dropna().round(3).drop_duplicates()

df_h1 = spark.createDataFrame(df4)
df_h1.write.format("orc").mode("overwrite").saveAsTable("stock_dw.baostock_daily_return")






