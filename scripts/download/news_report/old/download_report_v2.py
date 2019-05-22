## get all news report from the web
import csv
import datetime
import pandas as pd
import os
import urllib
import re
import sys
import time
#from functions import *
sys.path.append("../..")
from functions.connect_url import url_opener

#from package_path_define.path_define import *
#from package_downloaddata.download_data_v1 import save_dir1
#stdi, stdo, stde = sys.stdin, sys.stdout, sys.stderr
#reload(sys)
#sys.setdefaultencoding('utf-8')
#sys.stdin, sys.stdout, sys.stderr = stdi, stdo, stde
#script_path=os.path.dirname(os.path.realpath(__file__))

def find_url(stk_num):
    html1="http://vip.stock.finance.sina.com.cn/q/go.php/vReport_List/kind/search/index.phtml?symbol=%s&t1=all" %str(stk_num)
    soup2=url_opener(html1)
    a1=soup2.find_all('td',attrs={'class','tal f14'})
    return a1

import re
zhmodel = re.compile(u'[\u4e00-\u9fa5]')

def content_get(soup2):
    AllSpan=soup2.find_all('span')
    spantext=AllSpan[6]
    date=spantext.get_text()[3:]
    if len(date)==10:
        pass
    else:
        date=spantext.get_text().encode('latin1',"ignore").decode('gb2312',"ignore")[3:]
    text1=soup2.find_all('div',attrs={'class','blk_container'})
    text2=text1[0].get_text()
    match = zhmodel.search(text2)
    if match:
        textOut=text2
    else:
        textOut=text1[0].get_text().encode('latin1',"ignore").decode('gb2312',"ignore")
    return date,textOut
from dir_control.data_dir_v1 import data_dict,stk_index_list
import time
stk_index_list=[x for x in stk_index_list if str(x).zfill(6)[0]!='3']
k=0
for stk in stk_index_list[0:2]:
    stk=str(stk).zfill(6)
    conts=[]
    content1=find_url(stk)
    k=0
    for ss in content1:
        k+=1
        con_url=ss.find('a').get('href')
        soup2=url_opener(con_url)
        #conts.append(strs)
        date,textout=content_get(soup2)
        file1=str(stk)+'_'+str(date)+'_'+str(k)+'.txt'
        f=open(file1,'w')
        print(textout, file = f)
        f.close()
        print(k)
        time.sleep(2.5)

    #jieba.lcut(t3)
#date,textout=content_get(soup2)


'''

## wget the url and transform the string type, which can print chines
def wget_html(stk_num,date1,url1,k):
    html1=str(stk_num)+'_'+date1+'_'+k+'.html'
    #print html1
    os.system('wget '+url1+' -O index.html')
    os.system('iconv -f gbk -t utf-8 index.html >'+ html1)

def wget_html1(url):
    os.system('wget '+url+' -O index.html') ## get url save name to 'index.html'

def save_file(stk_num,date,k):
    html1=str(stk_num)+'_'+date+'_'+k+'.html'
    os.system('iconv -f gbk -t utf-8 index.html >'+ html1)

file1="news_report"
#market="shenzhen"
market="shanghai"
save_data_path1='\\'.join([main_path_data,file1])
if not os.path.exists(save_data_path1):
    os.makedirs(save_data_path1)

stock_path1='\\'.join([main_path_data,dir_stock_index,market])
sto2=os.listdir(stock_path1)
save_dir="./"
#stk_num="000001"
#sto2=["601398.sh","603787.sh"]
run_num=0
for stk_num in sto2:
    k=0
    run_num+=1
    sym=stk_num[0:6]
    print sym
    with open("\\".join([script_path,"log.sh"]), "a") as text_file:
        text_file.write("run "+str(run_num)+'  '+sym+'\n')
    save_dir_fi=save_dir1(save_data_path1,market,sym) ## make the dir
    try:
        url1=find_url(sym)
    except:
        url1='f'
    if len(url1)>=2:
        print len(url1)
        for a1 in url1:
            try:
                k+=1
                url2=a1.find('a').get('href')
                #print a2
                ## get the report date
                soup2=url_opener(url2)
                a1=soup2.find_all('span')
                a2=a1[6]
                date=a2.text[3:]
                #print a1
                text1=soup2.find_all('div',attrs={'class','blk_container'})
                file1=str(sym)+'_'+str(date)+'_'+str(k)+'.txt'
                f=open(file1,'w')
                for t1 in text1:
                    print >>f,t1
                f.close()
                time.sleep(2.5)
            except:
                pass
        os.system("mv -f *.txt "+save_dir_fi)
    else:
        print 'no data'

'''

'''
for a2 in url1[0:3]:
    #k+=1
    date1=a2.text
    #print date1
    try: ## try if the text can be transformed to datetime type
        date2=datetime.datetime.strptime(date1,'%Y-%m-%d')
        #print date2
        print k
        if date_define<date2:
            j+=1
            a2=url1[k-2] ## the url should be -2 to the date order
            url2=a2.find('a').get('href')
            wget_html(stk_num,date1,url2,str(j))
            print date1
            time.sleep(3)
    except:
        pass
    k+=1
'''

#print a2.text



