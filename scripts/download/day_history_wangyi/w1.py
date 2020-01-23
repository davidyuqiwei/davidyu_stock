from davidyu_cfg import *
from functions.connect_url import url_opener
#url = 'http://quotes.money.163.com/trade/lsjysj_002172.html?year=2007&season=4'
from functions.ForDownload import generate_stock_index,stk_index_list_gen
from functions.data_dir import *
#from dir_control.data_dir_v1 import data_dict
import time
from functions.make_dir import *
def download_data(stock_index,year,season):
    url = 'http://quotes.money.163.com/trade/lsjysj_%s.html?year=%s&season=%s'%(stock_index,str(year),str(season))
    soup1 = url_opener(url)
    table = soup1.find_all('table',\
            attrs={'class','table_bg001 border_box limit_sale'})
    all_tr = table[0].findAll('tr')
    str_in = []
    for i in all_tr:
        a1 = i.find_all('td')
        a2 = [x.get_text() for x in a1]
        str_in.append(a2)
    df1 = pd.DataFrame(str_in)
    df1 = df1.iloc[1:]
    df1['stock_index'] = stock_index
    return df1

def save_file_name(dir_name,stock_index,year,season):
    file_name1 = '_'.join([stock_index,year,season])
    file_name = os.path.join(dir_name,file_name1)+'.csv'
    return file_name
dir_day_history_wy = data_dict.get("day_history_wangyi")
stk_index_list = stk_index_list_gen()
year = [str(x) for x in range(1998,2020)]
season = [str(x) for x in [1,2,3,4]]

for stock_index in stk_index_list:
    print(stock_index)
    dir_name1 = os.path.join(dir_day_history_wy,stock_index)
    make_dir(dir_name1)
    for year1 in year:
        for season1 in season:
            try:
                df1 = download_data(stock_index,year1,season1)
                if df1.shape[0]>1:
                    file_name = save_file_name(dir_name,stock_index,year,season)
                    #print(file_name)
                    df1.to_csv(file_name,index=0)
            except:
                pass
            time.sleep(3)    
'''
stock_index = '601398'
year = 1880
season = 2
df1 = download_data(stock_index,year,season)

'''




