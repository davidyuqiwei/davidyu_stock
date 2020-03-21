from davidyu_cfg import *
from functions.pyspark_functions import *
from dazong_statistics_pyspark import *
sc = spark.sparkContext
sc.setLogLevel("ERROR")

sql1 = """
    select * from stock_dev.dazongjiaoyi 
    left join
    """

sql1 = """
    select * from stock_dev.dazongjiaoyi a
    left join
    (
    SELECT stock_index,stock_name,
    concat_ws('|', collect_set(gainian)) as all_gainian_list
    FROM stock_dev.gainian_bankuai
    GROUP BY stock_index,stock_name
    ) b
    on a.secucode = b.stock_index
    where stock_date = "2020-03-06"
"""
df1 = spark.sql(sql1)
df2 = df1.toPandas()

groupby_col = ["sname","secucode","buyername","zyl","priace","all_gainian_list"]
cols_out = ["sname","secucode","tval","all_gainian_list"]
df4,df5 = dadan_stats(df2,groupby_col,cols_out)
print(df5.head())


