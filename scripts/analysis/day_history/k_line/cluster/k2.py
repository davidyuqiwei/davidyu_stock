import pandas as pd
from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from sklearn.cluster import KMeans
from sklearn import metrics
import math
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AffinityPropagation
from collections import Counter

df1 = pd.read_csv("/home/davidyu/stock/data/test/dfcf_fuquan_kline_cluster.csv",sep=",")

column_names = ["stock_index", "dt","open","close","high","low"]
df1.columns = column_names
#df2 = df1[["stock_index", "dt",]]
df1["open_norm"] = df1["open"]/df1["low"]
df1["close_norm"] = df1["close"]/df1["low"]
df1["high_norm"] = df1["high"]/df1["low"]
df1["low_norm"] = df1["low"]/df1["low"]

def get_model(X,k):
    #kmeans_model = KMeans(n_clusters=k, init='k-means++')
    kmeans_model = KMeans(n_clusters=k)
    kmeans_model.fit(X)
    labels = kmeans_model.labels_
    return_data = {
                   "model":kmeans_model,
                    "label_data":labels
                    }
    return return_data
df2 = df1[["open_norm","close_norm","high_norm","low_norm"]]
r_data = get_model(df2.values,10)
model = r_data.get("model")
label_data = r_data.get("label_data")
X = df2.values
S = []
for k in range(2,22,2):
    print(k)
    r_data = get_model(X,10)
    model = r_data.get("model")
    label_data = r_data.get("label_data")
    S.append(metrics.silhouette_score(X, label_data, metric='euclidean'))

print(S)




