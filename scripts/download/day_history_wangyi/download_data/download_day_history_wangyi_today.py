from davidyu_cfg import *
from functions.connect_url import url_opener
#url = 'http://quotes.money.163.com/trade/lsjysj_002172.html?year=2007&season=4'
from functions.ForDownload import generate_stock_index,stk_index_list_gen
from functions.data_dir import *
#from dir_control.data_dir_v1 import data_dict
import time
from functions.make_dir import *
from functions.get_datetime import *
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

def do_download(stock_index,year1,season1):
    #print(stock_index)
    dir_name1 = os.path.join(dir_day_history_wy,stock_index)
    make_dir(dir_name1)
    try:
        df1 = download_data(stock_index,year1,season1)
        if df1.shape[0]>1:
            file_name = save_file_name(dir_name1,stock_index,str(year1),str(season1))
            df1.to_csv(file_name,index=0)
    except:
        print(stock_index+" not download")
        pass
def make_season(month):
    month = int(month)
    if month in [1,2,3]:
        seaon =1
    elif month in [4,5,6]:
        season = 2
    elif month in [7,8,9]:
        season = 3
    else:
        season = 4
    return season
if __name__ =='__main__':
    dir_day_history_wy = data_dict.get("day_history_wangyi")
    dir_name = dir_day_history_wy
    stk_index_list = stk_index_list_gen()
    now_date,_ = get_the_datetime()
    year = int(now_date.split("-")[0])
    month = int(now_date.split("-")[1])
    season = make_season(month)
    #stock_index ='000917'
    stock_index = sys.argv[1]
    stock_index = stock_index.zfill(6)
    do_download(stock_index,year,season)
'''
stock_index = '601398'
year = 1880
season = 2
df1 = download_data(stock_index,year,season)

'''




