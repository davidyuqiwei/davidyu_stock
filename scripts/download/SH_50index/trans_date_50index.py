from davidyu_cfg import *
import pandas as pd
from functions.get_datetime import *
now_date,now_date_time = get_the_datetime()
now_date = now_date.replace("_","-")

file1 = "000016cons.xls"
df1 = pd.read_excel(file1)
df1.columns = ["stock_date","index_code","index_name","index_name_en",\
        "stock_index","stock_name","stock_name_en","info"]
#print(df1.head())
df1['day'] = now_date
df1.to_csv("SH_50index.csv",index=0)
