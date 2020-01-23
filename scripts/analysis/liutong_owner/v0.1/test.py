from davidyu_cfg import *
from functions.pyspark_functions import *

sql1 = """
    select concat_ws('__',collect_list(owner_name)) as owner_name_list,
    concat_ws('__',collect_list(ratio)) ratio_list,
    stock_index from
    stock_dev.liutong_owner
    where dt ='2019-09-30'
    group by stock_index
"""

ss = spark.sql(sql1)
ss.show()
df1 = ss.toPandas()
df1.to_csv("owner_list.csv",index=0)

