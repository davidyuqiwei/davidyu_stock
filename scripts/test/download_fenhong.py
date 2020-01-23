import sys
import pandas as pd
from davidyu_cfg import *
from functions.connect_url import url_opener,driver_open
from functions.get_datetime import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
import requests
from bs4 import BeautifulSoup
#html1 = "http://data.10jqka.com.cn/ajax/sgpx/date/2019-06-30/ajax/1/free/1/"
import time

headers={
'Accept': 'text/html, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
'Connection': 'keep-alive',
'Cookie': 'srchGuide=sg; historystock=000778%7C*%7C60007C000910%7C*%7C603977%7C*%7C002687; Hm_lvt_60bad21af9c824a4a0530d5dbf4=1577769059,1577979951,1579019613; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1577769059,1577979951,1579019613; Hm_lvt_f79b64788a41577769059,1577979951,1579019613; Hm_lpvt_f79b64788a4e377c608617fba4c736e2=1579019971; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1579019971; Hm_lpvt_60bad21af9c824a4a0530d5dbf4357ca=1579019971; v=AsTNkUAqRqqxiPLmYLWbqk-ElUm23ehDqgJ8iN5lVE1TEWtzBu241_oRTB8t',
'hexin-v': 'AsTNkUAqRqqxiPLmYLWbqk-ElUm23ehDqgJ8iN5lVE1TEWtzBu241_oRTB8t',
'Host': 'data.10jqka.com.cn',
'Referer': 'http://data.10jqka.com.cn/financial/sgpx/',
'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'
}

season = ['03-31','06-30','09-30','12-31']
year = [str(x)+'-' for x in range(2003,2019)]

date_input = []
for year1 in year:
    for season1 in season:
        date_input.append(year1+season1)


#html1 = "http://data.10jqka.com.cn/ajax/sgpx/date/2019-12-31/ajax/2/free/1/"
def get_pages(date_input):
    html1 = "http://data.10jqka.com.cn/ajax/sgpx/date/%s/board/ALL/order/asc/page/1/ajax/1/free/1/"%(date_input)
    response=requests.get(html1, headers = headers) 
    #print(response.text)
    a1 = response.text
    soup = BeautifulSoup(a1)
    pages_num = 1
    try:
        pages = soup.find_all("span")[0].get_text().split("/")[1]
        pages_num = int(pages)
    except:
        pass
    return pages_num
def html_text(html1):
    response=requests.get(html1, headers = headers)
    a1 = response.text
    soup = BeautifulSoup(a1)
    return soup
def get_data(date_input):
    html1 = "http://data.10jqka.com.cn/ajax/sgpx/date/%s/board/ALL/order/asc/page/1/ajax/1/free/1/"%(date_input)
    page_num = get_pages(date_input)
    for i in range(1,page_num+1):
        html1 = "http://data.10jqka.com.cn/ajax/sgpx/date/%s/board/ALL/order/asc/page/%s/ajax/1/free/1/"%(date_input,i)
        soup = html_text(html1)
        print(soup)
        stock_name = [x.get_text() for x in soup.find_all("a",attrs={'class','J_showCanvas'})]
        if len(stock_name)>0:
	        df_list = []
	        for jj in range(1,len(stock_name)+1):
	            a1 = soup.find_all("tr")[jj]  
	            stock_name = a1.find_all("a",attrs={'class','J_showCanvas'})[0].get_text()
	            stock_code = a1.find_all("a",attrs={'class','stockCode'})[0].get_text()
	            six = [x.get_text().replace("\n","").replace(" ","") for x in a1.find_all("td",attrs={'class','tc'})]
	            zhuan_song = [ x.get_text() for x in a1.find_all("td",attrs={'class','tr'})]
	            df_list1 = [stock_code] + [stock_name]+ six[1:] + zhuan_song
	            df_list.append(df_list1)
	        df_out = pd.DataFrame(df_list)
	        ##  送股  每十股
	        df_out.columns = ['股票代码','股票简称','最新价','预计除权除息价',
	                '是否已分配','股权登记日','除权除息日','送股','转增股','送转总数','派息']
	        df_out.to_csv(date_input+'_'+str(i)+".csv",index=0)
        else:
            pass
        time.sleep(5)
import time
"""
for date_input1 in date_input[0:10]: 
    get_data(date_input1)
    time.sleep(10)
    #get_data("2019-06-30")
"""
#response=requests.get(html1)



#values={'act':'login'}

"""
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

"""

