from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from sklearn.cluster import KMeans
from sklearn import metrics
import math
import numpy as np
from davidyu_cfg import *
from functions.day_history.kLines import *
import itertools
from collections import Counter
## networkx
import networkx as nx
from functions.logModule.log_set import *
from sklearn.decomposition import PCA
from sklearn.preprocessing import Imputer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler



tmp_save_dir = tmp_data_dict.get("day_history_insert")
#df_all = pd.read_csv(os.path.join(tmp_save_dir,"kl_all_data.csv"),header=None)

df_all = pd.read_csv(os.path.join(tmp_save_dir,"kl_all_data.csv"),header=None,error_bad_lines=False,engine="python",nrows =1000)


df_all1 = df_all
df_all1.index = df_all.iloc[:,0].tolist()
df_all2 = df_all1.iloc[:,1:]



a1 = df_all2.T
a2 = a1
a2_float = a2.apply(lambda x:x.astype(float))
si = SimpleImputer()
si = SimpleImputer(strategy='mean') 

#imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
a2_input = si.fit_transform(a2_float.values)

scaler = StandardScaler()
scaler.fit(a2_input)
trans_data = scaler.transform(a2_input)

data_hash = []
for i in range(0,60):
    data_hash.append(hash(tuple(list(trans_data[:,i]))))



pca = PCA(n_components=10)
newX = pca.fit_transform(a2_input[:,500:600])
newX = pca.fit_transform(a2_input)

df_pca = pd.DataFrame(newX)

print(pca.explained_variance_ratio_)






a3 = a2.iloc[:,2:5]
a2_corr = a2.corr()

df_kl_corr_stack = pd.read_csv(os.path.join(tmp_save_dir,"kl_corr.csv"),converters={'stk1':str, 'stk2':str, 'corr':np.float16}).round(3)
df_kl_corr_stack1 = df_kl_corr_stack[(df_kl_corr_stack['corr']>0.95)&(df_kl_corr_stack['corr']<1)]

nodes = df_kl_corr_stack1['stk1'].unique().tolist()
edges = df_kl_corr_stack1.values.tolist() 
G1 = nx.Graph()
G1.add_weighted_edges_from(edges)
list_nw = list(nx.connected_components(G1))
#G1.add_nodes_from(nodes)
print(len(list_nw))
#most_common_len = Counter(list_nw).most_common(1)[0][0]

#G1.degree

df_connect = pd.DataFrame(list(G1.degree)) 
df_connect.columns = ['stk_index','degree']
df_connect.sort_values('degree')

#df_kl_corr_stack[df_kl_corr_stack['stk1'] == '600658']


df_high_corr = df_kl_corr_stack[(df_kl_corr_stack['stk1']=='603811')&(df_kl_corr_stack['corr']>0.95)]




df_slope = pd.read_csv(os.path.join(tmp_save_dir,"kl_pred_slope.csv"),converters={'slope':np.float16, 'stock_index':str})

df_corr_slope = pd.merge(df_high_corr,df_slope,left_on='stk2',right_on='stock_index')

df_corr_slope['slope'].aggregate(func=['sum','count','mean','min','std','max','quantile'])


df_corr_slope['slope'].quantile([0.1,0.2,0.4,0.5, 0.75])

#max(nx.connected_components(G1),key=len)
#[ x for x in G1.neighbors('600501') ]
#edges1 = edges[0:5]
#G = nx.Graph()  

'''
for n, nbrs in G1.adj.items():
    for nbr, eattr in nbrs.items():
         wt = eattr['weight']
         if wt >0.9: print('(%s, %s, %.3f)' % (n, nbr, wt))

'''



def matrix_norm():
    group.tolist()
    minVals = group.min(0)  # 为0时：求每列的最小值[0 3 1]   .shape=(3,)
    maxVals = group.max(0)  # 为0时：求每列的最大值[2 7 8]   .shape=(3,)
    ranges = maxVals - minVals
    m = group.shape[0]
    normDataSet = np.zeros(np.shape(group))       #  np.shape(group) 返回一个和group一样大小的数组，但元素都为0
    diffnormData =group - np.tile(minVals,(m,1))  #  (oldValue-min)  减去最小值
    normDataSet1 =diffnormData / np.tile(ranges,(m,1))





















