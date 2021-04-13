import pandas as pd
import sys
import gc
import os
#data_file = sys.argv[1] 
#df1 = pd.read_csv(data_file)

#df2 = df1[df1["price"]!="price"].drop_duplicates()
#df2.to_csv(data_file,index=0)

file_in=sys.argv[1]
save_file=sys.argv[2]
df1 = pd.read_csv(file_in)
df2 = df1[df1["price"]!="price"].drop_duplicates()
df2.to_csv(save_file,index=0)
#df2=df2.set_index("stock_index",drop=False)

#print(os.system("free -mh"))
#print(os.system("free -mh"))
#stock_list = df2["stock_index"].unique().tolist()
    #print(df2.shape)
    #print("##############"+i+"#############")
