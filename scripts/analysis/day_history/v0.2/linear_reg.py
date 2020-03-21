from pyspark import SparkConf, SparkContext 
from pyspark.sql import HiveContext,SparkSession 
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from pyspark.sql.types import *
from pyspark.sql.functions import pandas_udf, PandasUDFType
import pandas as pd
import numpy as np
from davidyu_cfg import *
from functions.pyspark_linear_regression import *

def slope_to_table(source_table,start_date,end_date,target_table):
    sql1= """ select * from %s where stock_date >= '%s'
        and stock_date <= '%s' """ %(source_table,start_date,end_date)
    my_dataframe = spark.sql(sql1)
    df1 = my_dataframe.select("adj_close","volume","stock_index")
    stock_index_slope = df1.select("stock_index","adj_close").groupby("stock_index").apply(single_linear_regression)
    #a4.show(50)
    stock_index_slope.registerTempTable("table1")
    droptable = """
            drop table if exists %s
    """%(target_table)
    spark.sql(droptable)
    sql2 = """create table %s as  select stock_index,adj_close 
        as slope, cnt as cnt, now() as stock_date from table1"""%(target_table)
    spark.sql(sql2)
if __name__ == "__main__":
    source_table = "stock_dev.day_history_insert"
    start_date = "2012-01-01"
    end_date = "2019-12-31"
    target_table = "stock_analysis.stock_linear_slope"
    slope_to_table(source_table,start_date,end_date,target_table)
    print("OK")  



'''
spark = SparkSession \
    .builder \
    .appName("davidyu") \
    .enableHiveSupport() \
    .getOrCreate()

sc=spark.sparkContext
sc.setLogLevel("ERROR")

'''

'''
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

'''
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
