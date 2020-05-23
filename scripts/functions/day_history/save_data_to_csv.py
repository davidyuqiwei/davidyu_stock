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
from functions.config import *

def loadSpark():
    spark = SparkSession \
        .builder \
        .appName("davidyu") \
        .enableHiveSupport() \
        .getOrCreate()
    
    sc = spark.sparkContext
    sc.setLogLevel("ERROR")
    return spark

def saveSparkSelectDataToCsv(stock_index,start_date,end_date,columns_in,save_path,file_name):
    logging.info("input stock index {}".format(str(stock_index)))
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
    df1.to_csv(os.path.join(save_path,file_name),index=0)
    #np.save(os.path.join(save_path,"select_DF.npy"),df1)

if __name__ == "__main__":
    '''
    @@ how to run @@
    spark-submit save_data_to_csv.py 'adj_close' "('300760', '300294')" '2020-01-02' '2020-12-12' 'test.csv'
    @ save path: save_path = tmp_data_dict.get("day_history")
    '''
    import argparse
    from davidyu_cfg import *
    from functions.data_dir import *
    from functions.config import *
    #save_path = os.path.split(os.path.abspath(__file__))[0]
    save_path = TMP_DATA_PATH['day_history_save_data_path']
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("columns_in",type=str,help="columns")
    parser.add_argument("stock_index",type=str,help="columns")
    parser.add_argument("start_date",type=str,help="columns")
    parser.add_argument("end_date",type=str,help="columns")
    parser.add_argument("file_name",default='spark_select_data.csv',type=str,help="columns")
    args = parser.parse_args()

    columns_in = args.columns_in
    stock_index = args.stock_index
    start_date = args.start_date
    end_date = args.end_date
    file_name = args.file_name
    slope_out = saveSparkSelectDataToCsv(stock_index,start_date,end_date,columns_in,save_path,file_name)
    print(slope_out)
