data_path="/home/davidyu/data/financial_report"
file_in="603955_2017.csv"

import os
import pandas as pd
df1=pd.read_csv(os.path.join(data_path,file_in))
df1=df1.replace("--",-9999).fillna(-9999)
df2=df1.T[1:]
df2.to_csv("test.csv",index=1,columns=None,header=None)
