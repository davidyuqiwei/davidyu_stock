from davidyu_cfg import *
from functions.connect_url import driver_open_noBS
from functions.connect_url import *
from bs4 import BeautifulSoup as BS
from functions.get_datetime import *
from functions.data_dir import *
#html = driver_open_noBS("http://data.eastmoney.com/gdfx/ShareHolderDetail.aspx?hdCode=80637337&hdName=%CF%E3%B8%DB%D6%D0%D1%EB%BD%E1%CB%E3%D3%D0%CF%DE%B9%AB%CB%BE")
#a1 = driver_open_noBS(html)  


columns_in = ['序号','代码','名称','最新价','涨跌额','涨跌幅','今开','最高','最低','昨结','成交量','成交额','买盘','卖盘','持仓量']
df_raw = pd.DataFrame(columns = columns_in)

html  = "http://data.eastmoney.com/xuangu/#Yz1bY3pfaHF6YjAxXXxzPWN6X2hxemIwMXxzdD0tMQ=="

a1 = driver_open_noBS(html)
soup1 = BS(a1.encode("gbk"))
a2 = soup1.find_all("table",attrs={'class','table_wrapper-table'})
soup1.find_all("td",attrs={'class','name'})
soup1.find_all("tr")

soup1.find_all("a",attrs={'target','_blank'})

soup1.find_all("td",attrs={'class','fav'})


soup1.find_all("td",attrs={'class','name'}) ## stock name

th id="cz_hqzb01_th"
a3 = a2[0]


len1 = len(a3.find_all('td'))
all_strings = []
k = 0
for i in range(0,len1):
    k+=1
    str1 = a3.find_all('td')[i].get_text()
    all_strings.append(str1)
    if len(all_strings)==15:
        df_raw.loc[i] = all_strings
        all_strings = [] 

now_date,now_date_time = get_the_datetime()
save_dir = data_dict.get("DFCF")
save_file = os.path.join(save_dir,"index_future_"+now_date+".csv")
df_raw.to_csv(save_file,index=0)
#print(df_raw)



