### download all owners
# coding: utf-8

# In[291]:


import csv
import datetime
import pandas as pd
import os
import urllib.request, urllib.parse, urllib.error
from functions import *
import re
import time
from package_path_define.path_define import *

#------- list the stock index we are get, for loop use
def list_stock_index(path_stock_index,market):
    stock_path=r'\\'.join([path_stock_index,market])
    print(stock_path)
    sto2=os.listdir(stock_path)
    return sto2
path_stock_owner_liutong=r'\\'.join([main_path,"data","stock_owner_liutong"])
if not os.path.exists(path_stock_owner_liutong):
    os.makedirs(path_stock_owner_liutong)
## create dir for save data it includes the time e.g.  /path/shenzhen/2017-01-01
def _save_dir(path_stock_owner,market):
    today=datetime.date.today()
    date1=str(today)
    save_dir=r'\\'.join([path_stock_owner,market,date1])
    print(('save_dir is '+save_dir))
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    return save_dir

def stk_owner(stock_id):
    stk=stock_id
    html1='http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CirculateStockHolder/stockid/%s.phtml' %stk
    print(html1)
    #html1='http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_StockHolder/stockid/'+i[0:6]+'/displaytype/30.phtml'
    soup2=url_opener(html1)
    t1=soup2.findAll("table",attrs={'id':'CirculateShareholderTable'})
    t2=t1[0]
    #t3=t2.findAll('tr',attrs={'class':'tr_2'})
    t3=t2.findAll('tr')
    owner=[]
    ratio=[]
    amount=[]
    date2=[]
    ## get the first date
    t5=t3[1]
    aa1=t5
    aa3=aa1.find_all('td')[0]
    date1=aa3.a.attrs['name']
    ####
    for t4 in t3:
        try:
            aa1=t4
            aa3=aa1.find_all('td')[0]
            date1=aa3.a.attrs['name']
            date3=date1
        except:
            date3=date1
        try:
            o1=t4.find_all('div')[1]
            a1=t4.find_all('div')[2]
            #print a1.text
            r1=t4.find_all('div')[3]
            owner.append(o1.text)
            amount.append(a1.text)
            ratio.append(r1.text)
            date2.append(date3)
        except:
            pass
            #print 'error'
    df1=pd.DataFrame({'Onwer':owner,"Amount":amount,"Ratio":ratio,"Date":date2})
    df2=df1[df1.Onwer!=df1.Onwer[0]]
    return df2

def save():
    ##----------save
    try:
        file_name1=i[0:6]+'.txt'
        file_name='\\'.join([save_dir,file_name1])
        info=open(file_name, 'a')
        all1=oo3+'  '+str(rr4)
        info.write(all1+'\n')
        info.close()
        time.sleep(8)
    except:
        print('error')






    #ownload_stock_owner(market,save_dir1)
    #market='shanghai'
    #download_stock_owner(path_stock_index,market,save_dir1)


# In[307]:


if __name__ == "__main__":
    #path_stock_index='../../../data/shanghai_shenzhen_data_from_2013/'
    #save_dir1='../../../data/stock_owner'
#------------------------------------------------------------
    market='shanghai'
    stk1=list_stock_index(path_stock_index,market)
    for stk in stk1:
        stk2=stk[0:6]
        df1=stk_owner(stk2)
        file_name=stk2+'_liutong.csv'
        df1.to_csv(file_name,index=False,sep=",",encoding='utf-8')
        file_name_tr=stk2+'_liutong_tr.csv'
        os.system('iconv -f utf-8 -t GB2312 '+file_name +' >'+file_name_tr)
        os.system('mv *.csv %s' %path_stock_owner_liutong)
        time.sleep(3)
#     print path_stock_owner_liutong


# In[281]:


stk="000661"
def stk_owner(stock_id):
    stk=stock_id
    html1='http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CirculateStockHolder/stockid/%s.phtml' %stk
    print(html1)
    #html1='http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_StockHolder/stockid/'+i[0:6]+'/displaytype/30.phtml'
    soup2=url_opener(html1)
    t1=soup2.findAll("table",attrs={'id':'CirculateShareholderTable'})
    t2=t1[0]
    #t3=t2.findAll('tr',attrs={'class':'tr_2'})
    t3=t2.findAll('tr')
    owner=[]
    ratio=[]
    amount=[]
    date2=[]
    ## get the first date
    t5=t3[1]
    aa1=t5
    aa3=aa1.find_all('td')[0]
    date1=aa3.a.attrs['name']
    ####
    for t4 in t3:
        try:
            aa1=t4
            aa3=aa1.find_all('td')[0]
            date1=aa3.a.attrs['name']
            date3=date1
        except:
            date3=date1
        try:
            o1=t4.find_all('div')[1]
            a1=t4.find_all('div')[2]
            #print a1.text
            r1=t4.find_all('div')[3]
            owner.append(o1.text)
            amount.append(a1.text)
            ratio.append(r1.text)
            date2.append(date3)
        except:
            pass
            #print 'error'
    df1=pd.DataFrame({'Onwer':owner,"Amount":amount,"Ratio":ratio,"Date":date2})
    df2=df1[df1.Onwer!=df1.Onwer[0]]
    return df2


# In[282]:


stk="000661"
df1=stk_owner(stk)
print(df1)


# In[266]:


stk="000661"
html1='http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CirculateStockHolder/stockid/%s.phtml' %stk
print(html1)
#html1='http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_StockHolder/stockid/'+i[0:6]+'/displaytype/30.phtml'
soup2=url_opener(html1)
t1=soup2.findAll("table",attrs={'id':'CirculateShareholderTable'})
t2=t1[0]
#t3=t2.findAll('tr',attrs={'class':'tr_2'})
t3=t2.findAll('tr')
owner=[]
date1=[]
ratio=[]
amount=[]
date2=[]
t5=t3[1]
aa1=t5
aa3=aa1.find_all('td')[0]
date1=aa3.a.attrs['name']
for t4 in t3:
    try:
        aa1=t4
        aa3=aa1.find_all('td')[0]
        date1=aa3.a.attrs['name']
        date3=date1
    except:
        date3=date1
    try:
        o1=t4.find_all('div')[1]
        a1=t4.find_all('div')[2]
        #print a1.text
        r1=t4.find_all('div')[3]
        owner.append(o1.text)
        amount.append(a1.text)
        ratio.append(r1.text)
        date2.append(date3)
    except:
        pass
        #print 'error'
df1=pd.DataFrame({'Onwer':owner,"Amount":amount,"Ratio":ratio,"Date":date2})


# In[269]:


date2


# In[222]:


a1.text


# In[250]:


t4=t3[1]
aa1=t4
aa3=aa1.find_all('td')[0]
date1=aa3.a.attrs['name']
date3=date1
print(date3)


# In[225]:


pd.DataFrame({'o1':owner,"a1":amount,"r1":ratio,"d1":date2})


# In[178]:


aa1=t3[1]
#print aa1
aa2=aa1.find_all('td')
#print aa2.find_all(attrs={'name'})
# print type(aa1)
# aa2=aa1.findAll("td",attrs={'width':'60'})
aa3=aa2[0]
print((type(aa3.a)))
aa3.a.attrs['name']
#aa2.name


# In[80]:


aa1=t3[10]
aa1.find_all('div')[2]


# In[ ]:


#market='shenzhen'
market='shanghai'
print((os.path.abspath(path_stock_index)))
##--- input
# 1. where the stock index located
# 2. which market we are interes 'shenzhen' ot 'shanghai'
# 3. where to save the data
download_stock_owner(path_stock_index,market,path_stock_owner)

