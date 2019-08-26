import os 
import pandas as pd
data_dir = "/home/davidyu/stock/data/test"
file1 = "all_test.csv"
file_in1 = os.path.join(data_dir,file1)

df1 = pd.read_csv(file_in1)
df_stand = df1[df1["x94"]==600519]

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from scipy import sparse


def CalSimi(df1,df2):
    df1 = df1.sort_values("x1")
    df2 = df2.sort_values("x1")
    a1 = df1[["x32","x33"]].values.reshape(-1)
    a2 = df2[["x32","x33"]].values.reshape(-1)
    # to cal    
    A= np.array([a1,a2])  
    A_sparse = sparse.csr_matrix(A)  
    similarities = cosine_similarity(A_sparse) 
    return similarities

simi_para = []
stk_index = []
for name,group in df1.groupby("x94"):
    stk_index.append(name)
    try:
        simi_score = CalSimi(group,df_stand)[0,1]
    except:
        simi_score = -999
    simi_para.append(simi_score)

df_dict={
        'stk_index': stk_index,
        'simi_score': simi_para
        }

df_out = pd.DataFrame(df_dict)
print(df_out.sort_values("simi_score",ascending=False).head(30))



'''
print(similarities)


file1 = "000917.csv"
file2 = "600519.csv"

file_in1 = os.path.join(data_dir,file1)
file_in2 = os.path.join(data_dir,file2)

df1 = pd.read_csv(file_in1)
df2 = pd.read_csv(file_in2)

'''


#a1 = np.array(df1.x33.tolist())
#a2 = np.array(df2.x33.tolist())


#cosine_similarity(a1,a2)


#from sklearn.metrics.pairwise import cosine_similarity

#cosine_similarity(a1,a2)
