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



#df_test= spark.sql("select * from stock_dev.day_history_insert where stock_index='000539;' and stock_date >= '2018-10-18' and stock_date <= '2018-11-19' ")
#df_test= spark.sql("select * from stock_dev.day_history_insert where stock_index='000539' ")

a2=spark.sql(""" select cast(stock_date as string),adj_close,stock_index from stock_dev.day_history_insert  """)

import datetime
'''
a2=df_test.toPandas()
a2['date']=a2['stock_date'].apply(lambda x:x.strftime('%Y-%m-%d'))

date1='2018-10-28'

start_date=datetime.datetime.strptime(date1,'%Y-%m-%d')
end_date=start_date+ datetime.timedelta(days=20)
start_date=start_date.strftime('%Y-%m-%d')
end_date=end_date.strftime('%Y-%m-%d')
'''
def get_start_end_date(start_date,linear_period):
    start_date=datetime.datetime.strptime(start_date,'%Y-%m-%d')
    end_date=start_date + datetime.timedelta(days=linear_period)
    start_date=start_date.strftime('%Y-%m-%d')
    end_date=end_date.strftime('%Y-%m-%d')
    return start_date,end_date

def linear_reg(df):
    rows=df.shape[0]
    x=np.array(range(rows)).reshape(-1,1)
    y = df.adj_close.values
    regr = linear_model.LinearRegression()
    regr.fit(x,y)
    fit1=round(regr.coef_.item(),3)
    return fit1
@pandas_udf("stock_date string,adj_close double,stock_index string ,future_reg double", PandasUDFType.GROUPED_MAP)
def future_linear_reg(a2):
    rows=a2.shape[0]
    #a2.stock_date = pd.to_datetime(a2.stock_date, format='%Y-%m-%d')
    linear_reg_list=[]
    #date1=[x.strftime('%Y-%m-%d') for x in df1.stock_date.values]
    for i in range(0,rows):
        try:
            date_in=a2.stock_date.values[i]
            start_date,end_date=get_start_end_date(date_in,5)
            df=a2[(a2['stock_date'] >= start_date) & (a2['stock_date'] <= end_date)]
            reg1=linear_reg(df)
        except:
            reg1=-9999
        linear_reg_list.append(reg1)
    ret_df = a2.assign(future_reg=linear_reg_list)
    return ret_df
a4=a2.groupby("stock_index").apply(future_linear_reg)
#a4.show(50)
import os
save_main_dir="/home/davidyu/stock/data/spark_out"
save_dir="future_linear_regression"
save_pred_dir=os.path.join(save_main_dir,save_dir)
a4.write.mode("overwrite").option("header", "true").parquet(save_pred_dir)

