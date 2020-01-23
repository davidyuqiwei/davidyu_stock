import pandas as pd
file1 = "000016cons.xls"
df1 = pd.read_excel(file1)
df1.columns = ["stock_date","index_code","index_name","index_name_en",\
        "stock_index","stock_name","stock_name_en","info"]
print(df1.head())
df1['day'] = '2019-12-17' 
df1.to_csv("SH_50index.csv",index=0)
