from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext,SparkSession
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from pyspark.sql.types import *
from pyspark.sql.functions import pandas_udf, PandasUDFType
import pandas as pd
import numpy as np
#https://github.com/sylitinglan/Moving-average-strategy
spark = SparkSession \
    .builder \
    .appName("davidyu") \
    .enableHiveSupport() \
    .getOrCreate()

sc=spark.sparkContext
sc.setLogLevel("ERROR")

table = "stock_dev.day_history_insert "
start_date = "2016-01-01"
end_date = "2018-12-21"
stock_index = "600663"


sql1= """
    select adj_close,volume,stock_index,stock_date from
    %s where stock_date >= '%s'
    and stock_date <= '%s' and stock_index = '%s'
""" %(table,start_date,end_date,stock_index)

a2 = spark.sql(sql1)


df = a2.toPandas()
df2 = df['adj_close']

ma_5 = df2.rolling(5).mean()
ma_10 = df2.rolling(10).mean()
ma_20 = df2.rolling(20).mean()
df4 = df['adj_close']
buy_sign=[]
for i in range(20,100):
    if ma_5[i]-ma_20[i]<0:
        i = i+1
        if ma_5[i]>=ma_20[i]:
            profit = (df4[i]-df4[i-1])/df4[i-1]
            profit_1 = str(profit)
            print('buy'+' '+profit_1)
            buy_sign.append(i)
            continue
        continue

print(df.loc[buy_sign,:])



