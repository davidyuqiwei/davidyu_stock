import pandas as pd
file1 = "000016cons.xls"
df1 = pd.read_excel(file1)
df1.columns = ["stock_date","index_code","index_name","index_name_en",\
        "stock_index","stock_name","stock_name_en","info"]
print(df1.head())
df1['day'] = '2019-12-17' 
df1.to_csv("SH_50index.csv",index=0)



import sys
import pandas as pd
from davidyu_cfg import *
from functions.connect_url import url_opener
from functions.get_datetime import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist

url1 = "http://vip.stock.finance.sina.com.cn/quotes_service/view/cn_bill_sum.php"
soup2 = url_opener(url1)

table = soup2.find_all('tbody')[1]


for row in table.find_all('tr'):
    column_marker = 0
    columns = row.find_all('td')
    for column in columns:
        column.get_text()column.get_text()








