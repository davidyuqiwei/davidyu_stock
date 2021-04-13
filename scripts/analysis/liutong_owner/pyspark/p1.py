from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext,SparkSession
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from pyspark.sql.types import *
from pyspark.sql.functions import pandas_udf, PandasUDFType
import pandas as pd
import numpy as np
from davidyu_cfg import *
from functions.LinearReg import LinearReg
from pyspark.sql.functions import *
## close SettingWithCopyWarning
pd.set_option('mode.chained_assignment', None)

spark = SparkSession \
    .builder \
    .appName("davidyu") \
    .enableHiveSupport() \
    .getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("ERROR")



sql1 = """
select owner_name,count(owner_name) as owner_name_cnt,
concat_ws(',',collect_set(t2.code)) as owner_list
from stock_dev.liutong_owner t1
left join stock.stock_index t2
on t1.stock_index = t2.code
where owner_name like '%全国社保%' and dt='2020-06-30'
group by owner_name
order by count(owner_name) desc

"""
df1 = spark.sql(sql1)

df2 = df1.toPandas()

x1 = df2.tail(10)["owner_list"].iloc[2]
x2 = x1.split(",")







