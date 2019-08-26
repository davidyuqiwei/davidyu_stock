## this script calculate all the stock trend over a period
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


#select x1,x33,x94 from stock_dev.fin_report where x1 >= '2015-01-01' and x1 <= '2018-11-19' and x94 = '603797'
from davidyu_cfg import *

@pandas_udf("x1 string,x94 string, x33 double,counts double", PandasUDFType.GROUPED_MAP)
def test1(df):
    import sys
    sys.path.append("/home/davidyu/stock/scripts/davidyu_stock/scripts")
    from LinearReg import LinearReg
    dfSort = df.sort_values("x1")  ## sort by date
    len_below_zero = len(dfSort[dfSort['x33']<0])  ## any profit is less than 0
    total_len = len(dfSort['x33'])  ## total rows of the dataframe
    if len_below_zero==0:
        dfForReg = pd.DataFrame(dfSort,columns=["x33"])
        linear_reg = LinearReg()
        slope, inter = linear_reg.single_linear_reg(dfForReg,"x33")
    else:
        slope = -9999
    ret_df = dfSort.assign(x33=slope).assign(counts=total_len).iloc[0:1,:]  ## only get the first result
    return ret_df


table = "stock_dev.fin_report "
start_date = '2015-01-01'
end_date = '2018-11-19'

# x1                     'stock date' 
# x33   float  COMMENT  '扣除非经常性损益后的净利润(元)',
# x94                    stock index
a2=spark.sql("""select x1,x33,x94 
        from %s where x1 >= '%s' and x1 <= '%s'
        """%(table,start_date,end_date))

a4=a2.select("x1","x94","x33").groupby("x94").apply(test1)

a4.sort("x33",ascending=False).show(300)
#a4.show()
#a4.registerTempTable("table1")  
#sql("create table stock_analysis.profit_table as  select * from table1")


