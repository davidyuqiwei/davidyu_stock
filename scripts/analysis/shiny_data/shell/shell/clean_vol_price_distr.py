import pandas as pd
import sys
import gc
import os
file_in=sys.argv[1]
save_file=sys.argv[2]
df1 = pd.read_csv(file_in)
df2 = df1[df1["price"]!="price"].drop_duplicates()
df2.to_csv(save_file,index=0)

