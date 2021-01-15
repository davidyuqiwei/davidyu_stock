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

sql2 = """
SELECT stock_date,stock_index,close,high,open,low,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 3 PRECEDING AND 1 PRECEDING),2) AS mv_avg3,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 5 PRECEDING AND 1 PRECEDING),2) AS mv_avg5,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 8 PRECEDING AND 1 PRECEDING),2) AS mv_avg8,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 13 PRECEDING AND 1 PRECEDING),2) AS mv_avg13,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 21 PRECEDING AND 1 PRECEDING),2) AS mv_avg21,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 34 PRECEDING AND 1 PRECEDING),2) AS mv_avg34,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 10 PRECEDING AND 1 PRECEDING),2) AS mv_avg10,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 15 PRECEDING AND 1 PRECEDING),2) AS mv_avg15,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 20 PRECEDING AND 1 PRECEDING),2) AS mv_avg20,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 30 PRECEDING AND 1 PRECEDING),2) AS mv_avg30,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 40 PRECEDING AND 1 PRECEDING),2) AS mv_avg40,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 50 PRECEDING AND 1 PRECEDING),2) AS mv_avg50,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 60 PRECEDING AND 1 PRECEDING),2) AS mv_avg60,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 120 PRECEDING AND 1 PRECEDING),2) AS mv_avg120,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 150 PRECEDING AND 1 PRECEDING),2) AS mv_avg150,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 200 PRECEDING AND 1 PRECEDING),2) AS mv_avg200,
round(avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 300 PRECEDING AND 1 PRECEDING),2) AS mv_avg300
from 
(
    select close,high,open,low,lpad(stock_index,6,'0') as stock_index,stock_date
    from
    stock_dev.dfcf_fuquan_byyear
    where 
    year >=2017 and lpad(stock_index,6,'0') in 
    (select stock_index from stock_dev.sample_stock_index)
)
"""


df_h1 = spark.sql(sql2)

#df_h1 = spark.createDataFrame(df4)
df_h1.write.format("orc").mode("overwrite").saveAsTable("stock_dw.dfcf_fuquan_mv_avg")






