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



table = "stock_dev.day_history_insert"
sql1= " select * from %s where stock_date >= '2018-10-18' and stock_date <= '2018-11-19' " %(table)
my_dataframe = spark.sql(sql1)

df1 = my_dataframe.select("adj_close","volume","stock_index")
'''
schema = StructType([
    StructField("stock_date", StringType()),
    StructField("adj_close", DoubleType()),
    StructField("volume", DoubleType()),
    StructField("stock_index", StringType())
])
'''

'''
schema = StructType([
    StructField("stock_index", StringType()),
    StructField("reg_coef", StringType())
])
'''
#a2= spark.sql("select adj_close,volume,stock_index from stock_dev.day_history_insert where stock_index='000539' and stock_date >= '2018-10-18' and stock_date <= '2018-11-19' ")
a2= spark.sql("select adj_close,volume,stock_index from stock_dev.day_history_insert where stock_date >= '2018-10-18' and stock_date <= '2018-11-19' ")

#df2=df1.toPandas()
@pandas_udf("stock_index string, adj_close double", PandasUDFType.GROUPED_MAP)
def test1(a1):
    X_in1 = pd.DataFrame(a1,columns=["adj_close"])
    X = pd.DataFrame(X_in1,columns=["adj_close"])
    # how many rows in the dataframe and make it as x
    rows = X_in1.shape[0]
    x = np.array(range(rows)).reshape(-1,1)
    #y = X_in1.loc[:, 'adj_close'].as_matrix(columns=None)
    y = X_in1.loc[:, 'adj_close'].values
    # regression
    regr = linear_model.LinearRegression()
    regr.fit(x,y)
    fit1 = round(regr.coef_.item(),3)
    ret_df = a1.assign(adj_close=fit1).iloc[0:1,:]  ## only get the first result
    return ret_df
a4 = a2.select("stock_index","adj_close").groupby("stock_index").apply(test1)
a4.show(50)

