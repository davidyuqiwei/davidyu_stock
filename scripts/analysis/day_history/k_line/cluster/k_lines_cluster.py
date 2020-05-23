from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from sklearn.cluster import KMeans
from sklearn import metrics
import math
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AffinityPropagation

data_dir = data_dict.get("day_history")

df1 = pd.read_csv(os.path.join(data_dir,"all.csv"),header=None)
df2 = df1.sample(10000)

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
    return X,df3

def get_model(k,X):
    #kmeans_model = KMeans(n_clusters=k, init='k-means++')
    kmeans_model = KMeans(n_clusters=k)
    kmeans_model.fit(X)
    labels = kmeans_model.labels_
    return kmeans_model
def dbscan(X,eps,min_samples):
    db = DBSCAN(eps=eps, min_samples=min_samples).fit(X)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_

    # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

    print('Estimated number of clusters: %d' % n_clusters_)
    #print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
    #print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
    #print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
    #print("Adjusted Rand Index: %0.3f"
    #              % metrics.adjusted_rand_score(labels_true, labels))
    #print("Adjusted Mutual Information: %0.3f"
    #              % metrics.adjusted_mutual_info_score(labels_true, labels))
    print("Silhouette Coefficient: %0.3f"
                  % metrics.silhouette_score(X, labels))
    return db

#metrics.silhouette_score(X,kmeans_model.labels_ , metric='euclidean')


def model_loss(X,kmeans_model):
    loss = 0
    for i in range(X.shape[0]):
        loss += np.sqrt(np.sum(np.square(X[i] - kmeans_model.cluster_centers_[kmeans_model.labels_[i]])))
    return loss 

def save_cluster(a1,k):
    df_k_type = pd.DataFrame(a1)
    df_k_type.columns = ["开盘价","盘高","盘低","收盘价","status"]
    df_k_type['日期'] = [x for x in range(1,df_k_type.shape[0]+1)]
    df_k_type = df_k_type[['日期',"开盘价","盘高","盘低","收盘价"]]
    df_k_type.to_csv("k_type_%s.csv"%(str(k)),index=0)


X,df_K= make_data(df2)
X = StandardScaler().fit_transform(X)
#db = dbscan(X,0.5,30)
#af = AffinityPropagation().fit(X) 


af = AffinityPropagation(preference=-25).fit(X) 

labels = af.labels_
df_K['labels'] = labels
print(max(labels))
df_out = df_K[["open","high","low","close","labels"]]
df_out.columns = ["开盘价","盘高","盘低","收盘价","labels"]
df_out.to_csv("AP_test.csv",index=0)
#df2['labels'] = labels


'''
kmeans 
for i in range(2,20):
    kmeans_model = get_model(i,X)
    loss = model_loss(X,kmeans_model)
    sil_score = metrics.silhouette_score(X,kmeans_model.labels_ , metric='euclidean')
    #print(i)
    print(str(i)+"|||"+str(round(loss,3))+'|||'+str(round(sil_score,3)))
    # print(sil_score)
    cluster_center = np.round(kmeans_model.cluster_centers_,2)
    save_cluster(cluster_center,i)

'''


#i = 14
#kmeans_model = get_model(i,X)
#a1 = np.round(kmeans_model.cluster_centers_,2)

#df3['labels'] = labels


def eucliDist(A,B):
    return math.sqrt(sum([(a - b)**2 for (a,b) in zip(A,B)]))

#a1 = df3[df3['labels'] ==9][["open","high","low","close"]].values


#df1.




