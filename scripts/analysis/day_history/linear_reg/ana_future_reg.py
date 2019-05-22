# https://www.cnblogs.com/pinard/p/6056319.html
from pyspark import SparkConf, SparkContext 
from pyspark.sql import HiveContext,SparkSession 
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from pyspark.sql.types import *
from pyspark.sql.functions import pandas_udf, PandasUDFType
import pandas as pd
import numpy as np
import os
spark = SparkSession \
    .builder \
    .appName("davidyu") \
    .enableHiveSupport() \
    .getOrCreate()

sc=spark.sparkContext
sc.setLogLevel("ERROR")

save_main_dir="/home/davidyu/stock/data/spark_out"
save_dir="future_linear_regression"

save_pred_dir=os.path.join(save_main_dir,save_dir)
df1=spark.read.parquet(save_pred_dir)

# get moving average
mv_avg=spark.sql(""" select * from stock_analysis.day_history_mv_avg""")

df1.registerTempTable("futureLR")
mv_avg.registerTempTable("mvAVG")

'''
com_df1=spark.sql("""
        select a.stock_index,a.stock_date,
        round(a.adj_close,2) as adj_close,
        future_reg,
        round(mv_avg5,2) as mv_avg5,
        round(mv_avg10,2) as mv_avg10,
        round(mv_avg15,2) as mv_avg15,
        round(mv_avg20,2) as mv_avg20,
        round(mv_avg30,2) as mv_avg30,
        round(mv_avg40,2) as mv_avg40,
        round(mv_avg50,2) as mv_avg50,
        round(mv_avg60,2) as mv_avg60,
        round(mv_avg120,2) as mv_avg120,
        round((mv_avg5-mv_avg10),2) as diff_d5_d10,
        round((mv_avg5-mv_avg60),2) as diff_d5_d60
        from futureLR a 
        left join mvAVG b
        where b.stock_index = a.stock_index and
        a.stock_date = b.stock_date
""")
'''
com_df1=spark.sql("""
        select a.stock_index,a.stock_date,
        round(a.adj_close,2) as adj_close,
        future_reg,
        round(mv_avg120,2) as mv_avg120,
        round((mv_avg5/mv_avg10),2) as diff_d5_d10,
        round((mv_avg5/mv_avg30),2) as diff_d5_d30,
        round((mv_avg5/mv_avg60),2) as diff_d5_d60,
        round((mv_avg5/mv_avg120),2) as diff_d5_120,
        round((mv_avg10/mv_avg30),2) as diff_d10_30,
        round((mv_avg10/mv_avg60),2) as diff_d10_60,
        round((mv_avg10/mv_avg120),2) as diff_d10_120
        from futureLR a 
        left join mvAVG b
        where b.stock_index = a.stock_index and
        a.stock_date = b.stock_date
""")

com_df1.registerTempTable("combDF")

tDF1=spark.sql(""" select * from combDF
        where stock_index= '601398' or stock_index = '000917'
""")

tt1=tDF1.toPandas()

tt2=tt1[tt1['stock_index']=='000917']
tt3=tt2.sort_values("stock_date").reset_index()
from scipy.signal import argrelextrema
a1=tt3.adj_close.values
index_max=argrelextrema(a1, np.greater,order=5) # find local maxima
index_min=argrelextrema(a1, np.less,order=5) # find local minima


tt4=tt3.assign(tag=0)


index_max_df=index_max[0].tolist()  

tt4.loc[index_max_df,['tag']]=1

column_in_train_model=["diff_d5_d10","diff_d5_d30","diff_d5_d60","diff_d5_120", \
        "diff_d10_30","diff_d10_60","diff_d10_120"]
column_in=column_in_train_model


test_num=int(np.floor(tt4.shape[0]*0.7))
train_df1=tt4.iloc[60:test_num,:]

train_X = pd.DataFrame(train_df1,columns=column_in).values.tolist()
train_Y = train_df1.tag.tolist()

from sklearn.ensemble import RandomForestRegressor


regr = RandomForestRegressor( random_state=1,n_jobs=5,n_estimators=10,max_features=5,
        min_samples_leaf=10,min_samples_split=10)

regr.fit(train_X, train_Y)


estimator = regr.estimators_[5]

print(regr.feature_importances_)


export_graphviz(estimator, out_file='tree.dot', 
rounded = True, proportion = False, 
precision = 2, filled = True)

from subprocess import call
call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png', '-Gdpi=600'])

from sklearn.model_selection import cross_val_score
scores1 = cross_val_score(regr, train_X, train_Y)
print(scores1.mean())


from sklearn.svm import SVR
regr_svr = SVR(gamma=0.01, C=1.0, epsilon=0.2)

scores1 = cross_val_score(regr_svr, train_X, train_Y)
print(scores1.mean())


