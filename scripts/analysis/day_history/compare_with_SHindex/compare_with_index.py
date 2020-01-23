## this script calculate a stock trend over a period
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
## close SettingWithCopyWarning
pd.set_option('mode.chained_assignment', None)  

spark = SparkSession \
    .builder \
    .appName("davidyu") \
    .enableHiveSupport() \
    .getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("ERROR")

def norm_col(df,col):
    return (df[col] - df[col].min())/(df[col].max() - df[col].min())

def stock_basic_info():
    sql1 = """
        select * from stock.stock_index
    """
    df1 = spark.sql(sql1)
    return df1

def SH_slope(SH_index_table,start_date,end_date):
    '''
    calculate the SH index slope give start and end date
    @ return SH_slope a float
    '''
    sql_SH_index = """
        select * from 
        %s where stock_date >= '%s'
        and stock_date <= '%s'
    """%(SH_index_table,start_date,end_date)
    SH_index_df = spark.sql(sql_SH_index)
    SH_index_df1 = SH_index_df.toPandas()
    SH_index_df1.loc[:,'norm_col'] = norm_col(SH_index_df1,'adj_close')
    SH_slope = LinearReg.single_linear_reg(SH_index_df1,'norm_col')[0]
    return SH_slope

def table_max_date(table):
    sql1 = """
    select max(stock_date) 
    from %s
    """%(table)
    max_time = spark.sql(sql1)
    print(max_time.show())

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

def apply_linear_reg(x):
    #x_in = x['adj_close']
    try:
        x.loc[:,'norm_col'] = norm_col(x,'adj_close')
        slope_out = LinearReg.single_linear_reg(x,'norm_col')[0]
    except:
        slope_out = -9999
    return slope_out


def every_stock_slope(df1,SH_slope):
    df_slope = []
    stock_index_loop = []
    stock_name = []
    industry = []
    for name,group in df1.groupby("stock_index"):
        a1 = apply_linear_reg(group)
        stock_index_loop.append(name)
        df_slope.append(a1)
        stock_name.append(group['name'].values[0])
        industry.append(group['industry'].values[0])
    data_dict = {
            'stock_index':stock_index_loop,
            'stock_name':stock_name,
            'industry':industry,
            'SH_slope':SH_slope,
            'slope':df_slope
        }
    df2 = pd.DataFrame(data_dict)
    return df2
if __name__ == "__main__":
	every_table = "stock_dev.day_history_insert"
	start_date = "2019-11-08"
	end_date = "2019-12-08"
	SH_index_table = "stock_dev.SH_index"
	table_max_date("stock_dev.day_history_insert")
	SH_slope = SH_slope(SH_index_table,start_date,end_date)
	df1 = get_data(every_table,start_date,end_date)
	#df_slope = df1.groupby('stock_index').apply(apply_linear_reg)
	#df2['slope']-SH_slope
	df2 = every_stock_slope(df1,SH_slope)
	df2['diff'] = df2['slope']-SH_slope
	df2 = df2.sort_values('diff',ascending=False)
	#target_table = "stock_analysis.reg_test"+"_"+start_date+"_"+end_date
	print(df2.head(20))


