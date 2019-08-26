import os 
import pandas as pd
data_dir = "/home/davidyu/stock/data/test"
file1 = "000917.csv"
file2 = "600519.csv"

file_in1 = os.path.join(data_dir,file1)
file_in2 = os.path.join(data_dir,file2)

df1 = pd.read_csv(file_in1)
df2 = pd.read_csv(file_in2)


from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from scipy import sparse
#a1 = np.array(df1.x33.tolist())
#a2 = np.array(df2.x33.tolist())

a1 = df1[["x32","x33"]].values.reshape(-1)
a2 = df2[["x32","x33"]].values.reshape(-1)

#a1 = a1/np.max(a1)
#a2 = a2/np.max(a2)

A= np.array([a1,a2])  
A_sparse = sparse.csr_matrix(A)  
similarities = cosine_similarity(A_sparse) 
print(similarities)

#cosine_similarity(a1,a2)


#from sklearn.metrics.pairwise import cosine_similarity

#cosine_similarity(a1,a2)
