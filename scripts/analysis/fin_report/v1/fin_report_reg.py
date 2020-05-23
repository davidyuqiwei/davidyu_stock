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



def make_the_DF(start_date,variable,source_table):
    sql1= """ select x1,round(%s,3) as adj_close,
        x94 as stock_index from %s where x1>'%s' and %s > -999
        order by x1 """ %(variable,source_table,start_date,variable)
    my_dataframe = spark.sql(sql1)
    df1 = my_dataframe.select("stock_index","adj_close")
    df3 = df1.groupby("stock_index").apply(single_linear_regression)
    return df3

def initTable(source_table):
    '''

    '''
    sql1 = "select distinct x94 as stock_index from %s"%(source_table)
    my_dataframe = spark.sql(sql1)
    return my_dataframe



source_table = "stock_dev.fin_report"
start_date='2012-01-01'
df_raw = make_table(source_table)
df_raw.registerTempTable("table1")

'''
loop for variables, and join to make the whole table
'''
for i in range(2,20):
    try:
	    variable = 'x'+str(i)
	    var_cnt = variable + '_cnt'
	    df3 = make_the_DF(start_date,variable,source_table)
	    df3.registerTempTable("table2")
	    sql2="""select table1.*,
        table2.adj_close as %s,
        table2.cnt as %s 
	    from table1 
        left join 
        table2
	    on table1.stock_index=table2.stock_index"""%(variable,var_cnt)
	    a2 = spark.sql(sql2)
	    a2.registerTempTable("table1")
    except:
        print("loop error")
        print("====================================================")
        print("the loop error is "+str(i))
        print("====================================================")
#sql3 = """select * from table1"""
#aa = spark.sql(sql3)
target_table = "stock_analysis.fin_report_linreg"
drop_table = "drop table if exists %s"%(target_table)
spark.sql(drop_table)
sql2 = """create table %s as select * from table1"""%(target_table)
spark.sql(sql2)
print("ok")

#ss = "select * from table1"
#dff = spark.sql(ss)
#print(aa.show(10))
    

#df2 = df1.select("x1","stock_index","adj_close").filter(df1['adj_close']>-999).filter(df1['stock_index']=='601288').sort('x1')

#df2 = df1.select("x1","stock_index","adj_close").filter(df1['adj_close']>-999)

#stock_index_slope = df1.select("stock_index","adj_close").filter(df1['adj_close']>-999).groupby("stock_index").apply(single_linear_regression)


