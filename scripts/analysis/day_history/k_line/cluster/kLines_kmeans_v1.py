from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from sklearn.cluster import KMeans
from sklearn import metrics
import math
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AffinityPropagation



def raw_data_col(df1):
    df1.columns = ["stock_date","high","low","open","close",
            "volume","adj_close","stock_index"]
    return df1

def make_data(df1):
    print(df1.shape)
    df1.columns = ["stock_date","high","low","open","close",
            "volume","adj_close","stock_index"]
    df2 = df1[["open","high","low","close"]]
    
    df3 = df2.div(df2.max(axis=1), axis=0)
    if 2==1:
        df3['status'] = df3['close'] - df3['open']
        df3['status'][df3['status']>0] = 1
        df3['status'][df3['status']<0] = -1
    df3 = df3.round(3)
    X = df3.values
    return X,df3

def get_model(k,X):
    #kmeans_model = KMeans(n_clusters=k, init='k-means++')
    kmeans_model = KMeans(n_clusters=k,n_init=100,init='k-means++',max_iter=1000)
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

def save_cluster(cluster_center,save_file):
    df_k_type = pd.DataFrame(cluster_center)
    #df_k_type.columns = ["开盘价","盘高","盘低","收盘价","status"]
    df_k_type.columns = ["开盘价","盘高","盘低","收盘价"]
    df_k_type['日期'] = [x for x in range(1,df_k_type.shape[0]+1)]
    df_k_type = df_k_type[['日期',"开盘价","盘高","盘低","收盘价"]]
    df_k_type.round(3).to_csv(save_file,index=0)

def eucliDist(A,B):
    return math.sqrt(sum([(a - b)**2 for (a,b) in zip(A,B)]))

def loop_k_stat():
    for i in range(10,14):
        kmeans_model = get_model(i,X)
        loss = model_loss(X,kmeans_model)
        sil_score = metrics.silhouette_score(X,kmeans_model.labels_ , metric='euclidean')
        #print(i)
        print(str(i)+"|||"+str(round(loss,3))+'|||'+str(round(sil_score,3)))
        # print(sil_score)
        cluster_center = np.round(kmeans_model.cluster_centers_,2)
        save_cluster(cluster_center,i)

def cluster_stat(x):
    rows = x.shape[0]
    dist_all = []
    for i in range(0,rows):
        dist1 = eucliDist(x.values[i][0],x.values[i][1])
        dist_all.append(dist1)
    max_dist = max(dist_all)
    median_dist = np.median(dist_all)
    x['max_dist'] = max_dist
    x['median_dist'] = median_dist
    x['cnt'] = rows
    return x.iloc[0,]
def cluster_center_dist(cluster_centers):
    center_cnt = len(cluster_centers)
    df_center_dist = pd.DataFrame(columns=["center1","center2","center_dist"])
    center_dist_list = []
    center1 = []
    center2 = []
    for i in range(0,center_cnt):
        for j in range(0,center_cnt):
            dist1 = eucliDist(cluster_centers[i],cluster_centers[j])
            center1.append(i)
            center2.append(j)
            center_dist_list.append(dist1)
    df_center_dist['center1'] = center1
    df_center_dist['center2'] = center2
    df_center_dist['center_dist'] = center_dist_list
    df_center_dist = df_center_dist[df_center_dist['center_dist']>0]
    df_center_dist = df_center_dist.sort_values('center_dist')
    return df_center_dist

def test(loop_num):
    data_dir = data_dict.get("day_history")
    df1 = pd.read_csv(os.path.join(data_dir,"all.csv"),header=None)
    df1 = raw_data_col(df1)
    df2 = df1[df1['stock_index']==600999]
    #df2 = df1.sample(10000)
      
    X,df_K = make_data(df2)
    n_cluster = 11
    kmeans_model = get_model(n_cluster,X)
    
    df_K['labels'] = kmeans_model.labels_
    #df2[["open","high","low","close"]].values
    df_K['raw_array'] = df_K[["open","high","low","close"]].values.tolist()
    #df_K['center'] = kmeans_model.cluster_centers_.tolist()
    df_cluster_cent_dist = cluster_center_dist(kmeans_model.cluster_centers_)
    print(df_cluster_cent_dist.iloc[0:3,])
    df_cluster_info = pd.DataFrame(columns=["label_center","labels"])
    df_cluster_info['label_center'] = kmeans_model.cluster_centers_.round(3).tolist()
    df_cluster_info['labels'] = [x for x in range(0,kmeans_model.n_clusters)]
    df_center = pd.merge(df_K,df_cluster_info,on='labels')[['raw_array',"label_center","labels"]]
    
    df_cluster_stat = df_center.groupby("labels").apply(cluster_stat)[["labels",'max_dist',"median_dist",'cnt']]
    print(df_cluster_stat.sort_values("max_dist",ascending=False))
    file_name = "cluster_%s_%s.csv"%(n_cluster,loop_num)
    save_cluster(kmeans_model.cluster_centers_,file_name)

if __name__ == "__main__":
    test(1)
