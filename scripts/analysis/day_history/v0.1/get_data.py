## this script calculate a stock trend over a period
'''
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

spark = SparkSession \
    .builder \
    .appName("davidyu") \
    .enableHiveSupport() \
    .getOrCreate()

'''
#from function import *
#from pyspark_head import *
from davidyu_cfg import *
from functions.pyspark_functions import *
sc = spark.sparkContext
sc.setLogLevel("ERROR")


def get_data(every_table,start_date,end_date):
    '''
    @param   every_table    hive table  --> day history table  e.g. "stock_dev.day_history_insert"
    @param   start_date     date string
    @param   end_date       date string
    
    @return  a python dataframe
    '''
    ##
    sql1= """
        select * from
        %s where stock_date >= '%s'
        and stock_date <= '%s' 
    """ %(every_table,start_date,end_date)
    #sql1="select * from stock_dev.SH_index"
    every_stock = spark.sql(sql1)
    df_basic = stock_basic_info()
    every_stock = every_stock.join(df_basic,df_basic.code==every_stock.stock_index)
    #every_stock.agg(max(col('stock_date'))).show()
    every_stock.agg(min(col('stock_date')),max(col('stock_date'))).show()
    every_stock_df = every_stock.toPandas()
    return every_stock_df

if __name__ =='__main__':
    every_table = "stock_dev.day_history_insert"
    start_date = "2019-09-30"
    end_date = "2019-12-08"
    df1 = get_data(every_table,start_date,end_date)
    print(df1.head(10))
    df1.to_csv("test_data.csv",index=0)

