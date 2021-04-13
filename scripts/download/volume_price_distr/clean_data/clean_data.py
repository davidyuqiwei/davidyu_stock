import pandas as pd
import sys
data_file = sys.argv[1] 
df1 = pd.read_csv(data_file)

df2 = df1[df1["price"]!="price"].drop_duplicates()
df2.to_csv(data_file,index=0)



