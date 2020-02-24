import sys
import os
import pandas as pd
import time
import datetime
import re
import time
zhmodel = re.compile(u'[\u4e00-\u9fa5]')  ## check if chines in the str
sys.path.append("../..")
from davidyu_cfg import *
from functions.connect_url import url_opener
#from dir_control.data_dir_v1 import data_dict,stk_index_list
from functions.data_dir import data_dict,create_dir_if_not_exist
from functions.stock_index_list import stk_index_list
import traceback
from functions.make_dir import *
import eventlet
eventlet.monkey_patch()
class html_content:
    html1 = "http://vip.stock.finance.sina.com.cn/q/go.php/vReport_List/kind/search/index.phtml?symbol=%s&t1=all&p=%d"
    def __init__(self,stock_index,page_num):
        self.html = self.html1%(stock_index,page_num)
    def find_url_content(self):
        soup2 = url_opener(self.html)
        a1 = soup2.find_all('td',attrs={'class','tal f14'})
        return a1
#content1 = html_content('000917',1).find_url_content()

class saveFile:
    def __init__(self,stock_index='',save_dir='',k='',date=''):
        self.stock_index = str(stock_index)
        self.save_dir = str(save_dir)
        self.date = str(date)
        self.k = str(k)  ## for some content in the same date loop to save the file name
    def news_report_save_dir(self):
        #file_name = str(self.stock_index)+'_'+str(date)+'_'+str(k)+'.txt'
        file_name = '_'.join([self.stock_index,self.date,self.k])+'.txt'
        save_file = os.path.join(self.save_dir,file_name)
        return save_file
#savefile = saveFile()

def content_get(soup2):
    AllSpan = soup2.find_all('span')
    spantext = AllSpan[6] ## date str
    date = spantext.get_text()[3:]
    if len(date) == 10:
        pass
    else:
        date = spantext.get_text().encode('latin1',"ignore").decode('gb2312',"ignore")[3:]
    text1=soup2.find_all('div',attrs={'class','blk_container'})
    text2=text1[0].get_text()
    match = zhmodel.search(text2)
    if match:
        textOut=text2
    else:
        textOut=text1[0].get_text().encode('latin1',"ignore").decode('gb2312',"ignore")
    return date,textOut

def news_in_html_url(url):
    con_url = 'http:'+url.find('a').get('href')
    soup2 = url_opener(con_url)
    date,textout = content_get(soup2)
    return date,textout

def content_to_txt(save_file,textout):
    f = open(save_file,'w')
    print(textout, file = f)
    f.close()

def get_all_news(stock_index,save_dir):
    #stk = '000917'
    make_dir(save_dir)
    for i in range(1,100):
        content1 = html_content(stock_index,i).find_url_content()  
        if len(content1)>0:
            k=0
            for url in content1:
                k += 1
                with eventlet.Timeout(2.5,False):
                    date,text_out = news_in_html_url(url)
                    saveFileTxt = saveFile(stock_index=stock_index,save_dir=save_dir,k=k,date=date).news_report_save_dir()
                    content_to_txt(saveFileTxt,text_out)
                    time.sleep(30)
        else:
            break  ## if no content break

def download_for_stock_index(stock_index):
    dir_news_report = data_dict.get("news_report")
    stk = stock_index
    try:
        get_all_news(stock_index,os.path.join(dir_news_report,stk))
    except Exception:
        print(stock_index+'not download')
        traceback.print_exc()
        pass
    time.sleep(3)
def main():
    for stk in stk_index_list:
        print(stk)
    print("finish")


if __name__ == '__main__':
    stock_index = sys.argv[1]
    download_for_stock_index(stock_index)
    #main()
