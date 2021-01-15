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
sql3 = """
select t1.*,
close/mv_avg3 as close_mvavg3,close/mv_avg5 as close_mvavg5,close/mv_avg8 as close_mvavg8,close/mv_avg13 as close_mvavg13,close/mv_avg21 as close_mvavg21,
high/mv_avg3 as high_mvavg3,high/mv_avg5 as high_mvavg5,high/mv_avg8 as high_mvavg8,high/mv_avg13 as high_mvavg13,high/mv_avg21 as high_mvavg21,
low/mv_avg3 as low_mvavg3,low/mv_avg5 as low_mvavg5,low/mv_avg8 as low_mvavg8,low/mv_avg13 as low_mvavg13,low/mv_avg21 as low_mvavg21,
open/mv_avg3 as open_mvavg3,open/mv_avg5 as open_mvavg5,open/mv_avg8 as open_mvavg8,open/mv_avg13 as open_mvavg13,open/mv_avg21 as open_mvavg21,
round(mv_avg3/mv_avg5,2) as mv_avg_3_5,
round(mv_avg3/mv_avg8,2) as mv_avg_3_8,
round(mv_avg3/mv_avg13,2) as mv_avg_3_13,
round(mv_avg5/mv_avg8,2) as mv_avg_5_8
from
stock_dw.dfcf_fuquan_mv_avg t1
"""


df_h1 = spark.sql(sql3)

#df_h1 = spark.createDataFrame(df4)
df_h1.write.format("orc").mode("overwrite").saveAsTable("stock_dw.dfcf_fuquan_mv_avg_feature")






