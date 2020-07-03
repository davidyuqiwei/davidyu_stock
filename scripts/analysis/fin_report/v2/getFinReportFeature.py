from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext,SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import pandas_udf, PandasUDFType
import pandas as pd
import numpy as np

spark = SparkSession \
    .builder \
    .appName("davidyu") \
    .enableHiveSupport() \
    .getOrCreate()

def getFinReportData(start_date,end_date):
    sql1 = """
        select 
        x3,x5,x7,x8,x9,x10,x11,x14,x16,x17,x21,
        x22,x23,x24,x26,x27,x31,x32,x36,x37,x38,
        x56,x59,x63,x64,x67,x68,x71,x72,x73,x79,x94
        from stock_dev.fin_report
        where x1>='%s' and x1<='%s'
        """%(start_date,end_date)
    my_dataframe = spark.sql(sql1)
    return my_dataframe
def transformData(my_dataframe):
    df1 = my_dataframe.toPandas()
    df2 = df1.fillna(-9999)
    #stock_index as index,   date,finicial features as columns
    df3 = df2.pivot_table(index=["x94"],columns=["x1"]).dropna()
    df4 = df3
    df4.columns = [x[0]+"_"+x[1] for x in df3.columns.tolist()]  
    ## select stock_index start with "0" and "60"
    stk_index = [x for x in df4.index.tolist() if x[0]=='0' or x[0:2]=='60']
    df5 = df4[df4.index.isin(stk_index)] 
    return df5

if __name__ == "__main__":
    from davidyu_cfg import *
    start_date = "2016-01-01"
    end_date = "2016-12-31"
    my_dataframe = getFinReportData(start_date,end_date)
    df5 = transformData(my_dataframe)
    df5['stock_index'] = df5.index.tolist()
    data_dir = tmp_data_dict.get("financial_report")
    file_name = "fin_report_feature.csv"
    save_file_name = os.path.join(data_dir,file_name)
    df5.to_csv(save_file_name,index=0)



