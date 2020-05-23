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

def stockLinearRegression(stock_index,start_date,end_date,columns_in,save_path):
    '''
    columns_in = "adj_close"
    stock_index = ("000545","601398","601318")
    start_date = "2018-09-02"
    end_date = "2018-09-12"
    '''
    spark = loadSpark()
    table = "stock_dev.day_history_insert"
    sql1= """ select %s,stock_date,stock_index from %s 
    where stock_date >= '%s' and stock_date <= '%s' and 
    stock_index in %s order by stock_date""" %(columns_in,table,start_date,end_date,stock_index)
    my_dataframe = spark.sql(sql1)
    df_cnt = my_dataframe.count()
    #logging.info("DATA FRAME rows".format(str(df_cnt)))
    df1 = my_dataframe.toPandas()
    np.save(os.path.join(save_path,"select_DF.npy"),df1)

if __name__ == "__main__":
    import argparse
    import os
    save_path = os.path.split(os.path.abspath(__file__))[0]
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("stock_index",type=str,help="columns")
    args = parser.parse_args()

    stock_index = args.stock_index
    print("input stock index")
    print(stock_index)
