from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext,SparkSession
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from pyspark.sql.types import *
from pyspark.sql.functions import pandas_udf, PandasUDFType
import pandas as pd
import numpy as np

spark = SparkSession \
    .builder \
    .appName("davidyu") \
    .enableHiveSupport() \
    .getOrCreate()

sc=spark.sparkContext
sc.setLogLevel("ERROR")

df=spark.sql(" select * from stock_analysis.day_history_mv_avg where stock_index='601398' ")

df1=df.toPandas() 

df1[df1.adj_close > df1.mv_avg5]

def strategy():

/*






