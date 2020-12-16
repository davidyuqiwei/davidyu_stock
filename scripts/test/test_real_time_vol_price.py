from davidyu_cfg import *
from functions.connect_url import url_opener
#url = 'http://quotes.money.163.com/trade/lsjysj_002172.html?year=2007&season=4'
from functions.ForDownload import generate_stock_index,stk_index_list_gen
from functions.data_dir import *
#from dir_control.data_dir_v1 import data_dict
import time
from functions.make_dir import *
from functions.get_datetime import *

html1 = "https://vip.stock.finance.sina.com.cn/quotes_service/view/vMS_tradedetail.php?symbol=sh600787&date=2020-12-10&page=16"

soup1 = url_opener(html1)
table = soup1.find_all('table',attrs={'class','datatbl'})


a1 = table[0].find_all("tr")[1] 
len1= len(table[0].find_all("tr"))
all_data = []
for i in range(1,len1):
	a1 = table[0].find_all("tr")[i]
    a1.find_all("th")
	time1 = a1.find_all("th")[0].get_text()
	status = a1.find_all("th")[1].get_text()
	price = a1.find_all("td")[0].get_text()
	volume = a1.find_all("td")[3].get_text()
	money = a1.find_all("td")[4].get_text()
	data1 = [time1,status,price,volume,money]
    all_data.append(data1)

df1 = pd.DataFrame(all_data)

