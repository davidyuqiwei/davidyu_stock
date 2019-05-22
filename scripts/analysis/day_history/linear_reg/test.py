from pyspark import SparkConf, SparkContext 
from pyspark.sql import HiveContext,SparkSession 

spark = SparkSession \
    .builder \
    .appName("davidyu") \
    .enableHiveSupport() \ 
    .getOrCreate()

sc=spark.sparkContext
sc.setLogLevel("ERROR")


#table1 = "stock_analysis.day_history_mv_avg "

table = "stock_dev.day_history_insert "
sql1= " select * from %s " %(table)

#println(sql1)


my_dataframe = spark.sql(sql1)

#my_dataframe.filter("stock_index=='000089'").show()

df1=my_dataframe.select("stock_date","adj_close","volume","stock_index")
import numpy as np

schema = StructType([
    StructField("stock_date", StringType()),
    StructField("adj_close", DoubleType()),
    StructField("volume", DoubleType()),
    StructField("stock_index", StringType())
])


a1=my_dataframe.filter("stock_index=='000089'").toPandas() 



a1=my_dataframe.filter("stock_index=='000089'")
my_dataframe.createGlobalTempView("test2")

a2= spark.sql("select * from stock_dev.day_history_insert where stock_index='000539' and stock_date >= '2018-10-18' and stock_date <= '2018-11-19' ")

a1=a2.toPandas()
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
import pandas as pd
@pandas_udf(schema, PandasUDFType.GROUPED_MAP)
def test1(a1):
    X_in1= pd.DataFrame(a1,columns=["stock_date","adj_close","volume","stock_index"])
    X=pd.DataFrame(X_in1,columns=["stock_date"])
    out_df=pd.DataFrame(columns=('stock_index', 'predict'))
    # how many rows in the dataframe and make it as x
    rows=X_in1.shape[0]
    x=np.array(range(rows)).reshape(-1,1)
    y = X_in1.loc[:, 'adj_close'].as_matrix(columns=None)
    # regression
    regr = linear_model.LinearRegression()
    regr.fit(x,y)
    fit1=regr.coef_.item()
    out_df.loc[0]=[X_in1.stock_index.values[0],fit1]
    return out_df
a4=df2.groupby("city").apply(test1)


training = spark.read.format("libsvm").load("/home/davidyu/software/spark-2.4.0-bin-hadoop2.7/data/mllib/sample_libsvm_data.txt")



glr = GeneralizedLinearRegression(family="gaussian", link="identity", maxIter=10, regParam=0.3)

model = glr.fit(dataset)


sql1='select * from stock_analysis.day_history_std'

my_dataframe.sort("std_close",ascending=False).show()




