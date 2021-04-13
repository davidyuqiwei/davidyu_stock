import pandas as pd
df1=pd.read_csv("/home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/dfcf_fuquan/modelling/v1/predict_out.csv")
df2=df1[df1['stock_index']!='stock_index']
df3 = df2.sort_values("result").drop_duplicates()
df3.to_csv("predict_out.csv",index=0)
#print(df3)

