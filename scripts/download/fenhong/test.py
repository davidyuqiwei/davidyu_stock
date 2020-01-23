import sys
import pandas as pd
from davidyu_cfg import *
from functions.connect_url import url_opener,driver_open
from functions.get_datetime import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
import requests
from bs4 import BeautifulSoup
html1 = "http://data.10jqka.com.cn/ajax/sgpx/date/2019-06-30/ajax/1/free/1/"
#html1 = "http://data.10jqka.com.cn/ajax/sgpx/date/2019-03-31/ajax/1/free/1/"

headers={
'Accept': 'text/html, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
'Connection': 'keep-alive',
'Cookie': 'searchGuide=sg; historystock=000778%7C*%7C600061%7C*%7C000910%7C*%7C603977%7C*%7C002687; Hm_lvt_60bad21af9c824a4a0530d5dbf4357ca=1577769059,1577979951,1579019613; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1577769059,1577979951,1579019613; Hm_lvt_f79b64788a4e377c608617fba4c736e2=1577769059,1577979951,1579019613; Hm_lpvt_f79b64788a4e377c608617fba4c736e2=1579019971; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1579019971; Hm_lpvt_60bad21af9c824a4a0530d5dbf4357ca=1579019971; v=AsTNkUAqRqqxiPLmYLWbqk-ElUm23ehDqgJ8iN5lVE1TEWtzBu241_oRTB8t',
'hexin-v': 'AsTNkUAqRqqxiPLmYLWbqk-ElUm23ehDqgJ8iN5lVE1TEWtzBu241_oRTB8t',
'Host': 'data.10jqka.com.cn',
'Referer': 'http://data.10jqka.com.cn/financial/sgpx/',
'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'
}


response=requests.get(html1, headers = headers) 
print(response.text)
a1 = response.text
soup = BeautifulSoup(a1)
#soup.find_all("td")

#zhuang_song = [x.get_text() for x in soup.find_all("td",attrs={'class','tr'})]

#first_six = [x.get_text().replace("\n","").replace(" ","") for x in soup.find_all("td",attrs={'class','tc'})]

stock_name = [x.get_text() for x in soup.find_all("a",attrs={'class','J_showCanvas'})]
#stock_code = [x.get_text() for x in soup.find_all("a",attrs={'class','stockCode'})]


df_list = []
for i in range(1,len(stock_name)+1):
    a1 = soup.find_all("tr")[i]  
    stock_name = a1.find_all("a",attrs={'class','J_showCanvas'})[0].get_text()
    stock_code = a1.find_all("a",attrs={'class','stockCode'})[0].get_text()
    six = [x.get_text().replace("\n","").replace(" ","") for x in a1.find_all("td",attrs={'class','tc'})]
    zhuan_song = [ x.get_text() for x in a1.find_all("td",attrs={'class','tr'})]
    df_list1 = [stock_code] + [stock_name]+ six + zhuan_song
    df_list.append(df_list1)

df_out = pd.DataFrame(df_list)






#response=requests.get(html1)



#values={'act':'login'}


