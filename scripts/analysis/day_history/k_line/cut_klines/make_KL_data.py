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
from sklearn.preprocessing import scale
from sklearn.cluster import KMeans
import datetime
from functions.logModule.log_set import *

def clean_dict_data(kline_dict,most_common_len):
    '''
    clean the K-line data,keep the data has same length
    '''
    for j in list(kline_dict.keys()):
        if len(kline_dict[j]['kline_data']) != most_common_len:
            kline_dict.pop(j)
    return kline_dict

def kline_data_dict(list_files,para):
    '''
    K-line data  every day open,high,low,close flat
    and the return predict slope
    '''
    data_list_len = []
    kline_dict = {}
    kline_return = {}
    for i in range(0,len(list_files)):
        try:
            stk_index = list_files[i][0:6]
            df1 = pd.read_csv(os.path.join(data_dir,list_files[i]),header=None)
            kline_data = kLine(df1,para)
            df_selectTime = kline_data.set_column_name().data_select(para.get('stat_start_date'),para.get('stat_end_date'))
            df2 = df_selectTime.get_kline_data()
            pred_slope = kline_data.linearRegPred()
            group = df2.values
            data_list = list(itertools.chain(*group.tolist()))
            kline_return = {}
            kline_return['kline_data'] = data_list
            kline_return['pred_slope'] = pred_slope
            kline_dict[stk_index] = kline_return
            data_list_len.append(len(data_list))
        except:
            print(list_files[i][0:6])
            pass
    return kline_dict,data_list_len
def clean_dict(kline_dict,data_list_len):
    #for i in kline_dict:
    data_list_len1 = [x for x in data_list_len if x >0]
    most_common_len = Counter(data_list_len1).most_common(1)[0][0]
    logging.info("dict out")
    logging.info(kline_dict)
    kline_data_dict = clean_dict_data(kline_dict,most_common_len)
    return kline_data_dict

if __name__ =='__main__':
    data_dir = data_dict.get("day_history_insert")
    list_files = os.listdir(data_dir)
    '''
    @k-line high,close,low,open    start_date,end_date
    @predict the slope      start_date,end_date
    '''
    kl_stat_day=14
    kl_pred_day=7
    stat_start_date = "2017-03-01"
    #klineDate = klineDate(stat_start_date,kl_stat_day,kl_pred_day)
    stat_end_date,pred_start_date,pred_end_date = klineDate(stat_start_date,kl_stat_day,kl_pred_day).make_date()
    
    para = {
        'stat_start_date':stat_start_date,
        'stat_end_date':stat_end_date,
        'pred_start_date':pred_start_date,
        'pred_end_date':pred_end_date
        }

    kline_dict,data_list_len = kline_data_dict(list_files,para)
    
    keys = list(kline_dict.keys())

    KLINE_data = [x.get('kline_data')  for x in kline_dict.values()]
    pred_slope_data = [x.get('pred_slope')  for x in kline_dict.values()]
    ## k-lines data
    df_kl = pd.DataFrame(KLINE_data).T
    df_kl.columns = keys 
    tmp_save_dir = tmp_data_dict.get("day_history_insert")
    df_kl.to_csv(os.path.join(tmp_save_dir,"kl_data.csv"),index=0)
    
    # the slope trend under the k-lines
    df_pred_slope = pd.DataFrame(pred_slope_data,columns=['slope'])
    df_pred_slope['stock_index'] = keys
    df_pred_slope.to_csv(os.path.join(tmp_save_dir,"kl_pred_slope_v2.csv"),index=0)
    # k-lines correlation
    df_kl_corr = df_kl.corr().round(2)
    df_kl_corr_stack = df_kl_corr.stack().reset_index()
    df_kl_corr_stack.columns = ['stk1','stk2','corr']
    df_kl_corr_stack.to_csv(os.path.join(tmp_save_dir,"kl_corr.csv"),index=0)


################################################################################
'''
df_kl_cluster = df_kl.T
data = scale(df_kl_cluster.values)
df_kl_cluster_norm = pd.DataFrame(data)
df_kl_cluster_norm.index = df_kl_cluster.index
df_kl_cluster_norm.round(2).to_csv(os.path.join(tmp_save_dir,"kl_cluster_norm.csv"),index=0)
#df_kl_cluster['labels'].to_csv("kl_cluster_label.csv")


'''




## networkx
'''
import networkx as nx
df_kl_corr_stack1 = df_kl_corr_stack[(df_kl_corr_stack['corr']>0.9)&(df_kl_corr_stack['corr']<1)]

nodes = df_kl_corr_stack1['stk1'].unique().tolist()
edges = df_kl_corr_stack1.values.tolist() 
G1 = nx.Graph()
G1.add_weighted_edges_from(edges)
list(nx.connected_components(G))

'''

'''
# kmeans test

from sklearn.preprocessing import scale
from sklearn.cluster import KMeans
data = scale(df_kl_cluster.values)

n_digits = 5
kmeans = KMeans(init='k-means++', n_clusters=n_digits, n_init=10)
kmeans.fit(data)
kmeans.labels_

'''








'''
#[ x for x in G1.neighbors('600501') ]
edges1 = edges[0:5]
G = nx.Graph()  

G.add_weighted_edges_from(edges1)
list(nx.connected_components(G))

G1.add_weighted_edges_from(edges)
for n, nbrs in G1.adj.items():
    for nbr, eattr in nbrs.items():
         wt = eattr['weight']
         if wt >0.9: print('(%s, %s, %.3f)' % (n, nbr, wt))

'''
























