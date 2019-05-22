import pandas as pd
a1=pd.read_csv("all.csv")

#### transform to chinese
def tr(x):
    x1=x.encode('latin1',"ignore").decode('gb2312',"ignore")
    return x1

a1.iloc[:,1]=a1.iloc[:,1].apply(tr)
a1.iloc[:,2]=a1.iloc[:,2].apply(tr)
a1.iloc[:,3]=a1.iloc[:,3].apply(tr)
a1.iloc[:,4]=a1.iloc[:,4].apply(tr)
a1.to_csv("all_tr.csv",index=0,header=None)
