from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from sklearn.cluster import KMeans
from sklearn import metrics
import math
import numpy as np
data_dir = data_dict.get("day_history")

df1 = pd.read_csv(os.path.join(data_dir,"all.csv"),header=None)
df2 = df1.sample(100000)

def make_data(df1):
    print(df1.shape)
    df1.columns = ["stock_date","high","low","open","close",
            "volume","adj_close","stock_index"]
    df2 = df1[["open","high","low","close"]]
    
    df3 = df2.div(df2.max(axis=1), axis=0)
    df3['status'] = df3['close'] - df3['open']
    df3['status'][df3['status']>0] = 1
    df3['status'][df3['status']<0] = -1
    
    df3 = df3.round(3)
    X = df3.values
    return X

def get_model(k,X):
    kmeans_model = KMeans(n_clusters=k)
    kmeans_model.fit(X)
    labels = kmeans_model.labels_
    return kmeans_model
#metrics.silhouette_score(X,kmeans_model.labels_ , metric='euclidean')


def model_loss(X,kmeans_model):
    loss = 0
    for i in range(X.shape[0]):
        loss += np.sqrt(np.sum(np.square(X[i] - kmeans_model.cluster_centers_[kmeans_model.labels_[i]])))
    return loss 


X = make_data(df2)
for i in range(2,20):
    kmeans_model = get_model(i,X)
    loss = model_loss(X,kmeans_model)
    sil_score = metrics.silhouette_score(X,kmeans_model.labels_ , metric='euclidean')
    #print(i)
    print(str(i)+"|||"+str(round(loss,3))+'|||'+str(round(sil_score,3)))
    # print(sil_score)

#df3['labels'] = labels


def eucliDist(A,B):
    return math.sqrt(sum([(a - b)**2 for (a,b) in zip(A,B)]))

#a1 = df3[df3['labels'] ==9][["open","high","low","close"]].values


#df1.




