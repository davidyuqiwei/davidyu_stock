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

#table = "stock_dev.fin_report "
#sql1= " select * from %s where stock_date >= '2018-10-18' and stock_date <= '2018-11-19' " %(table)
#my_dataframe = spark.sql(sql1)

#df1=my_dataframe.select("x1","x33","x94")
#a2= spark.sql("select adj_close,volume,stock_index from stock_dev.day_history_insert where stock_index='000539' and stock_date >= '2018-10-18' and stock_date <= '2018-11-19' ")

# x33   float  COMMENT  '扣除非经常性损益后的净利润(元)',

a2=spark.sql("select x1,x33,x94 from stock_dev.fin_report where x1 >= '2015-01-01' and x1 <= '2018-11-19' ")

@pandas_udf("x1 string,x94 string, x33 double", PandasUDFType.GROUPED_MAP)
def test1(a1):
    a1=a1.sort_values("x1")
    len1=len(a1[a1['x33']<0])
    if len1==0:
	    X_in1=pd.DataFrame(a1,columns=["x33"])
	    X=pd.DataFrame(X_in1,columns=["x33"])
	    # how many rows in the dataframe and make it as x
	    rows=X_in1.shape[0]
	    x=np.array(range(rows)).reshape(-1,1)
	    #y = X_in1.loc[:, 'adj_close'].as_matrix(columns=None)
	    y1 = X_in1.loc[:, 'x33'].values
	    y=y1/max(y1)
	    # regression
	    regr = linear_model.LinearRegression()
	    regr.fit(x,y)
	    fit1=round(regr.coef_.item(),3)
    else:
        fit1=-9999
    ret_df=a1.assign(x33=fit1).iloc[0:1,:]  ## only get the first result
    return ret_df
a4=a2.select("x1","x94","x33").groupby("x94").apply(test1)
a4.sort("x33",ascending=False).show(50)

a4.registerTempTable("table1")  
sql("create table stock_analysis.profit_table as  select * from table1")


