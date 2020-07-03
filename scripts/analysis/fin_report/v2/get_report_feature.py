from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext,SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import pandas_udf, PandasUDFType
import pandas as pd
import numpy as np

sql1 = """
    select x1,x3,x5,x7,x8,x9,x10,
    x11,x14,x16,x17,x21,x22,x23,x24,x26,
    x27,x31,x32,x36,x37,x38,x56,x59,x63,x64,x67,
    x68,x71,x72,x73,x79,x94
    from stock_dev.fin_report
    where x1>='2016-01-01' and x1<='2016-12-31'
    """
my_dataframe = spark.sql(sql1)

df1 = my_dataframe.toPandas()
df2 = df1.fillna(-9999)

def cnt_it(x):
    try:
        cnt = x[x>-999].shape[0]
    except:
        cnt = 100
    return cnt

#df2.apply(lambda x:cnt_it(x),axis=0)
#df1.pivot_table(index=["x94"],columns=["x1"])
df3 = df2.pivot_table(index=["x94"],columns=["x1"])
df4 = df3.dropna()
df4.columns = [x[0]+"_"+x[1] for x in df4.columns.tolist()]  
stk_index = [x for x in df4.index.tolist() if x[0]=='0' or x[0]=='6']
df4[df4.index[0] in stk_index]

df5 = df4[df4.index.isin(stk_index)] 

from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
from sklearn import metrics
data = scale(df5.values)

n_digits = 10
kmeans = KMeans(init='k-means++', n_clusters=n_digits, n_init=10)
kmeans.fit(data)
kmeans.labels_


from sklearn.decomposition import PCA
pca = PCA(0.8)
pca.fit(data)
X_data = pca.transform(data).shape
X_data = pca.transform(data)

n_digits = 10
kmeans = KMeans(init='k-means++', n_clusters=n_digits, n_init=10)
kmeans.fit(X_data)
kmeans.labels_

metrics.silhouette_score(data, kmeans.labels_, metric='euclidean')

df_out = pd.DataFrame([df5.index.tolist(),kmeans.labels_.tolist()]).T
df_out.columns = ["stock_index","label"]

df_out[df_out["stock_index"] == "600519"]
df_out[df_out["label"]==3]


from sklearn.feature_selection import VarianceThreshold

sel = VarianceThreshold(threshold=1)
a1 = sel.fit_transform(data)


'''
for i in range(0,10):
    print(len(np.where(kmeans.labels_==i)[0]))

'''

df_out = pd.DataFrame([df4.index.tolist(),kmeans.labels_.tolist()]).T
df_out.columns = ["stock_index","label"]

df_out[df_out["stock_index"] == "600519"]
df_out[df_out["label"]==8]




metrics.silhouette_score(data, kmeans.labels_, metric='euclidean')


from sklearn.cluster import DBSCAN

y_pred = DBSCAN(eps = 5, min_samples = 10).fit_predict(data)

df_out = pd.DataFrame([df4.index.tolist(),y_pred.tolist()]).T
df_out.columns = ["stock_index","label"]
df_out.groupby('label').count()

metrics.silhouette_score(data, y_pred, metric='euclidean')

df_out[df_out["stock_index"] == "600519"]
df_out[df_out["label"]==-1]

