import csv
import datetime
import pandas as pd
import os
import urllib.request, urllib.parse, urllib.error
from functions import *
import re
import time
from package_path_define.path_define import *
import traceback
#------- list the stock index we are get, for loop use
def list_stock_index(path_stock_index,market):
    stock_path=r'\\'.join([path_stock_index,market])
    print(stock_path)
    sto2=os.listdir(stock_path)
    return sto2
path_stock_owner_liutong=r'\\'.join([main_path,"data","stock_owner_liutong"])
if not os.path.exists(path_stock_owner_liutong):
    os.makedirs(path_data_backup1)
## create dir for save data it includes the time e.g.  /path/shenzhen/2017-01-01
def _save_dir(path_stock_owner,market):
    today=datetime.date.today()
    date1=str(today)
    save_dir=r'\\'.join([path_stock_owner,market,date1])
    print(('save_dir is '+save_dir))
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    return save_dir

def download_stock_owner(path_stock_index,market,save_dir):
    sto2=list_stock_index(path_stock_index,market)
    save_dir='./'
    for i in sto2[0:2]:
        try:
            sym=i[0:6]
            html1='http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CirculateStockHolder/stockid/%s/displaytype/30.phtml' %sym
            print(html1)
            #html1='http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_StockHolder/stockid/'+i[0:6]+'/displaytype/30.phtml'
            soup2=url_opener(html1)
            #soup2=soup2.encode("GBK", 'ignore')
            #print(soup2)
            t1=soup2.findAll("table",attrs={'id':'CirculateShareholderTable'})
            t2=t1[0]
            #print(t2)
            #t3=t2.findAll('tr',attrs={'class':'tr_2'})
            t3=t2.findAll('tr')
            a1=t3[4:17]  ## top 10 owners
            owner=[]
            ratio=[]
            for a2 in a1:
                a4=a2.findAll('td')
                oo1=a4[1]
                oo2=oo1.text
                oo3=oo2.encode('utf-8')  ## name of the onwers company
                owner.append(oo3)
                rr1=a4[3]
                rr2=rr1.text
                rr3 = re.findall(r'\d+\.\d+',rr2) ## find the number is d.d, e.g.  1.5; 2.3
                rr4=float(rr3[0])
                ratio.append(rr4)
                ##----------save
                file_name1=i[0:6]+'.txt'
                file_name='\\'.join([save_dir,file_name1])
                info=open(file_name, 'a')
                print((type(oo3)))
                print((type(rr4)))
                all1=oo3+b"\n\n"+bytes(str(rr4),encoding="utf-8")
                info.write(str(all1,encoding="utf-8")+'\n')
                info.close()
            time.sleep(8)
        except Exception as e:
            print((str(e)))
            traceback.print_exc()

if __name__ == "__main__":
    #path_stock_index='../../../data/shanghai_shenzhen_data_from_2013/'
    #save_dir1='../../../data/stock_owner'
#------------------------------------------------------------
    #market='shenzhen'
    market='shanghai'
    print((os.path.abspath(path_stock_index)))
    ##--- input
    # 1. where the stock index located
    # 2. which market we are interes 'shenzhen' ot 'shanghai'
    # 3. where to save the data
    download_stock_owner(path_stock_index,market,path_stock_owner)




    #ownload_stock_owner(market,save_dir1)
    #market='shanghai'
    #download_stock_owner(path_stock_index,market,save_dir1)
