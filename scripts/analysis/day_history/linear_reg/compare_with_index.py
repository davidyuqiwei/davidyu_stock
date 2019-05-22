## this script calculate a stock trend over a period
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


table = "stock_dev.SH_index"
start_date= "2017-01-01"
end_date="2018-02-21"

sql1= """
    select adj_close,volume from
    %s where stock_date >= '%s'
    and stock_date <= '%s' 
""" %(table,start_date,end_date)



sql1="select * from stock_dev.SH_index"
a2=spark.sql(sql1)
df1=a2.toPandas()

#target_table = "stock_analysis.reg_test"+"_"+start_date+"_"+end_date


def single_linear_reg(df,column_in):
    X_in1=pd.DataFrame(df,columns=[column_in])
    X=pd.DataFrame(X_in1,columns=[column_in]).dropna()
    # how many rows in the dataframe and make it as x
    rows=X.shape[0]
    x=np.array(range(rows)).reshape(-1,1)
    y = X.values
    # regression
    regr = linear_model.LinearRegression()
    regr.fit(x,y)
    fit1=round(regr.coef_.item(),3)
    return fit1
lm1=single_linear_reg(df1,"adj_close")
print(lm1)
#target_table = "stock_analysis.reg_test"+"_"+start_date+"_"+end_date
#target_table = "stock_analysis.reg_test"+"_"+start_date+"_"+end_date

"""
a2=spark.sql(sql1)

a4=a2.select("stock_index","adj_close").groupby("stock_index").apply(test1)
#a4.show(50)
a4.registerTempTable("table1")


sql2="create table %s as  select * from table1" %(target_table)
spark.sql(sql2)

"""



