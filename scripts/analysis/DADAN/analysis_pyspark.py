from davidyu_cfg import *
from functions.pyspark_functions import *
from analysis_today_update import *

sql1 = """
select * from stock_test.dadan_100 
where day>='2020-01-01'  and day <='2020-02-05'
and stock_index='600516'
""" 
df1 = spark.sql(sql1)
# print the random data
df1.orderBy(rand()).limit(10).show()
#df1.sample(False, 0.5, seed=0).limit(50).show()
df2 = df1.toPandas()
df_merge1 = DADAN_diff_stat(df2)





