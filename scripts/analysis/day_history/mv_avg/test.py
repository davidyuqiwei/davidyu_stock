from pyspark import SparkConf, SparkContext 
from pyspark.sql import HiveContext,SparkSession 
spark = SparkSession \
    .builder \
    .appName("davidyu") \
    .getOrCreate()

sc=spark.sparkContext
sc.setLogLevel("ERROR")


table1 = "stock_analysis.day_history_mv_avg "

table = "stock_dev.day_history_insert "
sql1= " select * from %s " %(table)

#println(sql1)


my_dataframe = spark.sql(sql1)

my_dataframe.filter("stock_index=='000089'").show()


import numpy as np

schema = StructType([
    StructField("city", StringType()),
    StructField("date", StringType()),
    StructField("predict", DoubleType())
])



from sklearn.linear_model import LinearRegression
from sklearn import linear_model
@pandas_udf(schema, PandasUDFType.GROUPED_MAP)
def test1(a1):
    X_in1= pd.DataFrame(a1,columns=["year","month","weekday","city","fill_sale_qty"])
    X=pd.DataFrame(X_in1,columns=["year"])
    out_df=pd.DataFrame(columns=('city', 'date', 'predict'))
    rows=X_in1.shape[0]
    x=np.array(range(rows)).reshape(-1,1)
    y = X_in1.loc[:, 'fill_sale_qty'].as_matrix(columns=None)
    regr = linear_model.LinearRegression()
    regr.fit(x,y)
    fit1=regr.coef_.item()
    out_df.loc[0]=[X_in1.city.values[0],'linear',fit1]
    #out_df.loc[1]=[X_in1.city.values[0],'real',20]
    #out_df.loc[2]=[X_in1.city.values[0],'pred',2]
    return out_df
a4=df2.groupby("city").apply(test1)


training = spark.read.format("libsvm").load("/home/davidyu/software/spark-2.4.0-bin-hadoop2.7/data/mllib/sample_libsvm_data.txt")



glr = GeneralizedLinearRegression(family="gaussian", link="identity", maxIter=10, regParam=0.3)

model = glr.fit(dataset)


sql1='select * from stock_analysis.day_history_std'

my_dataframe.sort("std_close",ascending=False).show()




