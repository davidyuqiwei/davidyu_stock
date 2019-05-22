# coding: utf-8
# %load download_financial.py
import csv
import datetime
import pandas as pd
import os
import urllib.request, urllib.parse, urllib.error
from functions import *
import re
import time
from write_to_csv import *
import sys
import pickle
from package_path_define.path_define import *
from package_downloaddata.download_data_v1 import save_dir1
import imp
from copy_the_data_v1 import *
'''
stdi, stdo, stde = sys.stdin, sys.stdout, sys.stderr
imp.reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdin, sys.stdout, sys.stderr = stdi, stdo, stde
'''
def find_url(url):
    #print html1
    soup2=url_opener(url)
    a1=soup2.find_all(id='BalanceSheetNewTable0')
    #print(a1)
    #a1=soup2.findAll('table',attrs={'class','tb_01'})
    #a1=soup2.findAll('td')
    soup1=a1[0]
    return soup1

def download_table(html,stk_num,year,save_dir):
    #print(html)
    soup1=find_url(html)
    rows=soup1.find_all('tr')
    data=[]
    for row in rows:
        cols=row.find_all('td')
        cols = [ele.text.strip() for ele in cols] ## get every data in the rows
        data.append([ele for ele in cols if ele]) ## make a list for data to save
        #print cols
    #print(data)
    myfile=os.path.join(save_dir,stk_num+'_'+year+'.csv')
    myfile_tr=os.path.join(save_dir,stk_num+'_'+year+'_tr.csv')
    write_to_csv(myfile,data)
    os.system("sed -i '1d' "+myfile)  ## remove the first line, which is blank
    os.system("sed -i '2d' "+myfile)  ## remove the second line
    #os.system('iconv -f utf-8 -t GB2312 %s > %s' %(myfile,myfile_tr))
    #os.system('iconv -f -t GB2312 -t utf-8 %s > %s' %(myfile,myfile_tr))
    print(myfile)
    #os.system('mv *.csv '+move_dir)
    return myfile
print('load module and functions')

## set the visited records
if os.path.isfile('visited.pkl'):
    pkl_file = open('visited.pkl', 'rb')
    visited = pickle.load(pkl_file)
else:
    visited=set()
    output = open('visited.pkl', 'wb')
    pickle.dump(visited, output)
    # Pickle the list using the highest protocol available.
    #pickle.dump(selfref_list, output, -1)
    output.close()

## set not visited
if os.path.isfile('not_visited.pkl'):
    pkl_file = open('not_visited.pkl', 'rb')
    not_visited = pickle.load(pkl_file)
else:
    not_visited=set()
    output2 = open('not_visited.pkl', 'wb')
    pickle.dump(not_visited, output2)
    # Pickle the list using the highest protocol available.
    #pickle.dump(selfref_list, output, -1)
    output2.close()


#market="shenzhen"
market="shanghai"
stock_path1='\\'.join([main_path_data,dir_stock_index,market])
sto2=os.listdir(stock_path1)


## save the data in current folder and move to ...
save_dir='./'

dir1="financial_report"
save_data_path1='\\'.join([main_path_data,dir1])
#download_table(stk_num,'csv_table')
#html_base="http://vip.stock.finance.sina.com.cn/corp/go.php/vFD_FinancialGuideLine/stockid/%s/displaytype/4.phtml"
html_base="http://money.finance.sina.com.cn/corp/go.php/vFD_FinancialGuideLine/stockid/%s/ctrl/%s/displaytype/4.phtml"
#year=xrange(1990,2017)
year=[2017]
#sto2=['000917']
folder1="financial_report"

def find_market(stk):
    if stk.startswith('00'):
        market='shenzhen'
    elif stk.startswith('60'):
        market='shanghai'
    else:
        print('wrong input stock number')
    return market
for stk_num in sto2[1100:]:
    for year1 in year:
        try:
            sym=stk_num[0:6]
            #print sym
            html1=html_base %(str(sym),str(year1))
            #if html1 not in visited:
            file_name=download_table(html1,sym,str(year1),save_dir)   ## download
            market=find_market(stk_num)
            print(market)
            ### copy the data to
            copy_data_to_foler(folder1,market,sym,file_name)
            #print move_dir_fi
            time.sleep(3)
            # save the visited files
            # Pickle the list using the highest protocol available.
        except Exception as e:
            print(stk_num)
    os.system('rm -rf *.csv')
'''
        except Exception as e:
            not_visited = not_visited | {html1}
            print(Exception, ":",e)
            output2 = open('not_visited.pkl', 'r+b')
            pickle.dump(not_visited, output2)
            output2.close()
            print('not donwload')
'''

#find -type d -empty  ## find the empty folder

