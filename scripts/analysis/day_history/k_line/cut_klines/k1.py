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
data_dir = data_dict.get("day_history")
list_files = os.listdir(data_dir)
kline_dict = {}
#all_file = "all.csv"

i=1
start_date = "2003-01-01"
end_date = "2006-03-31"
data_list_len = []

'''
K-line data
'''
for i in range(0,100):
    stk_index = list_files[i][0:6]
    df1 = pd.read_csv(os.path.join(data_dir,list_files[i]),header=None)
    kline_data = kLine(df1)
    df2 = kline_data.set_column_name().get_kline_data(start_date,end_date)
    #kl_data = df2.kline_data(start_date,end_date)
    group = df2.values
    data_list = list(itertools.chain(*group.tolist()))
    kline_dict[stk_index] = data_list
    data_list_len.append(len(data_list))
#for i in kline_dict:
most_common_len = Counter(data_list_len).most_common(1)[0][0]

for j in list(kline_dict.keys()):
    if len(kline_dict[j]) !=  most_common_len:
        kline_dict.pop(j)
        
df_kl = pd.DataFrame.from_dict(kline_dict)

def matrix_norm():
    group.tolist()
    minVals = group.min(0)  # 为0时：求每列的最小值[0 3 1]   .shape=(3,)
    maxVals = group.max(0)  # 为0时：求每列的最大值[2 7 8]   .shape=(3,)
    ranges = maxVals - minVals
    
    m = group.shape[0]
    normDataSet = np.zeros(np.shape(group))       #  np.shape(group) 返回一个和group一样大小的数组，但元素都为0
    diffnormData =group - np.tile(minVals,(m,1))  #  (oldValue-min)  减去最小值
    normDataSet1 =diffnormData / np.tile(ranges,(m,1))





















