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
from functions.logModule.log_set import *
def loadSpark():
    spark = SparkSession \
        .builder \
        .appName("davidyu") \
        .enableHiveSupport() \
        .getOrCreate()
    
    sc = spark.sparkContext
    sc.setLogLevel("ERROR")
    return spark

def stockLinearRegression(stock_index,start_date,end_date,columns_in):
    '''
    columns_in = "adj_close"
    stock_index="000545"
    start_date = "2018-09-02"
    end_date = "2018-09-12"
    '''
    spark = loadSpark()
    table = "stock_dev.day_history_insert"
    sql1= """ select %s,stock_date from %s 
    where stock_date >= '%s' and stock_date <= '%s' and 
    stock_index = '%s' order by stock_date""" %(columns_in,table,start_date,end_date,stock_index)
    my_dataframe = spark.sql(sql1)
    df_cnt = my_dataframe.count()
    #logging.info("DATA FRAME rows".format(str(df_cnt)))
    if df_cnt == 0:
        logging.info("no data find out")
        return -999
    else:
        logging.info("DATA FRAME rows {}".format(str(df_cnt)))
        df1 = my_dataframe.toPandas()
        df1['norm_col'] = (df1['adj_close']-df1['adj_close'].min())/(df1['adj_close'].max()-df1['adj_close'].min()+0.001)
        logging.info(df1.head(10))
        logging.info(df1.tail(10))
        slope_out = LinearReg.single_linear_reg(df1,'norm_col')[0]
        np.save("slope_out.npy",slope_out)
    return slope_out

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("columns_in",type=str,help="columns")
    parser.add_argument("stock_index",type=str,help="columns")
    parser.add_argument("start_date",type=str,help="columns")
    parser.add_argument("end_date",type=str,help="columns")
    args = parser.parse_args()

    columns_in = args.columns_in
    stock_index = args.stock_index
    start_date = args.start_date
    end_date = args.end_date
    print(stock_index)
    slope_out = stockLinearRegression(stock_index,start_date,end_date,columns_in)
    print(slope_out)
