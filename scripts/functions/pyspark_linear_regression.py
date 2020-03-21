from pyspark.sql.functions import pandas_udf, PandasUDFType
import pandas as pd
from sklearn import linear_model
from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext,SparkSession
import numpy as np
spark = SparkSession \
    .builder \
    .appName("davidyu") \
    .enableHiveSupport() \
    .getOrCreate()

sc=spark.sparkContext
sc.setLogLevel("ERROR")


@pandas_udf("stock_index string, adj_close double,cnt int", PandasUDFType.GROUPED_MAP)
def single_linear_regression(a1):
    #df_out = pd.DataFrame(columns = ["stock_index","adj_close","cnt"])
    try:
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
	    ret_df['cnt'] = rows
    except:
        ret_df = a1.assign(adj_close=-999).iloc[0:1,:]
        ret_df['cnt'] = -999
    return ret_df
