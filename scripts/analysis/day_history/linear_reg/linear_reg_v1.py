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



@pandas_udf("stock_index string, adj_close double", PandasUDFType.GROUPED_MAP)
def test1(a1):
    X_in1=pd.DataFrame(a1,columns=["adj_close"])
    X=pd.DataFrame(X_in1,columns=["adj_close"])
    # how many rows in the dataframe and make it as x
    rows=X_in1.shape[0]
    x=np.array(range(rows)).reshape(-1,1)
    #y = X_in1.loc[:, 'adj_close'].as_matrix(columns=None)
    y = X_in1.loc[:, 'adj_close'].values
    # regression
    regr = linear_model.LinearRegression()
    regr.fit(x,y)
    fit1=round(regr.coef_.item(),3)
    ret_df=a1.assign(adj_close=fit1).iloc[0:1,:]  ## only get the first result
    return ret_df

def SQL_v1(table,start_date,end_date):
    sql1= """
        select adj_close,volume,"600001" as stock_index from
        %s where stock_date >= '%s'
        and stock_date <= '%s' 
    """ %(table,start_date,end_date)
    return sql1

table = "stock_dev.SH_index"
start_date= "2018-02-02"
end_date="2018-12-28"
#target_table = "stock_analysis.reg_test"+"_"+start_date+"_"+end_date
sql1=SQL_v1(table,start_date,end_date)
a2=spark.sql(sql1)

#a4=a2.select("stock_index","adj_close").groupby("stock_index").apply(test1)
a4=a2.select("stock_index","adj_close").groupby("stock_index").apply(test1)
#a4=a2.select("stock_index","adj_close").apply(test1)
#a4.show(50)
#a4.registerTempTable("table1")


#sql2="create table %s as  select * from table1" %(target_table)
#spark.sql(sql2)



