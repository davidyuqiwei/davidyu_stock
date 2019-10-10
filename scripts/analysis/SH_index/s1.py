import scipy
import pandas as pd
import os
import numpy as np
from scipy import misc


data_dir = "/home/davidyu/stock/data/test"
file_name = "SH_index_test.csv"

df1 = pd.read_csv(os.path.join(data_dir,file_name))
#df1 = df1.head(100)
df2 = df1[["open","high","low","close","volume"]]


#df_norm2 = df2.apply(lambda x: (x - np.mean(x)) / (np.std(x)))

df_norm2 = df2.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))

df_mat = df_norm2.values *255
df_mat = df_mat.transpose()
#import Image
from PIL import Image
import matplotlib.pyplot as plt
im = Image.fromarray(df_mat)
new_p = im.convert('L')
new_p =  new_p.resize((800,800))
new_p.save('test.png')

'''
scipy.misc.imsave('a.jpg', df_mat)
misc.imsave('a.jpg', df_mat)

'''





