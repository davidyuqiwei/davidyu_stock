import sys
import os
import pandas as pd
import time
import datetime
import re
import time
zhmodel = re.compile(u'[\u4e00-\u9fa5]')  ## check if chines in the str
sys.path.append("../..")
from functions.connect_url import url_opener
from dir_control.data_dir_v1 import data_dict,stk_index_list
def find_url(stk_num):
    html1="http://vip.stock.finance.sina.com.cn/q/go.php/vReport_List/kind/search/index.phtml?symbol=%s&t1=all" %str(stk_num)
    soup2=url_opener(html1)
    a1=soup2.find_all('td',attrs={'class','tal f14'})
    return a1


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
def save_data(save_dir,file_name):
    import os
    save_file_name=os.path.join(save_dir,file_name)

def process(stk):
    dir_liutong_news_report=data_dict.get("news_report")
    dir_v1=os.path.join(dir_liutong_news_report,str(stk))
    ## if dir exist pass 
    if os.path.exists(dir_v1):
        pass
    else:
        conts=[]
        content1=find_url(stk)
        k=0
        for ss in content1:
            k+=1
            con_url=ss.find('a').get('href')
            soup2=url_opener(con_url)
            #conts.append(strs)
            date,textout=content_get(soup2)
            file_name=str(stk)+'_'+str(date)+'_'+str(k)+'.txt'
            os.system("mkdir -p %s" %(str(dir_v1)))
            #os.system("mv %s %s" %(dir_liutong_news_report+"/"+str(stk)+"*",dir_v1))
            save_file=os.path.join(dir_v1,file_name)
            f=open(save_file,'w')
            print(textout, file = f)
            f.close()
            time.sleep(2.5)
def main():
    from dir_control.data_dir_v1 import data_dict,stk_index_list
    import traceback
    dir_liutong_news_report=data_dict.get("news_report")
    dir_news_report=data_dict.get("news_report")
    stk_index_list=[x for x in stk_index_list if str(x).zfill(6)[0]!='3']
    stk_index_list.reverse()
    for stk in stk_index_list:
        stock_index=str(stk).zfill(6)
        try:
            process(stock_index)
        except Exception:
            print(stock_index+'not download')
            traceback.print_exc()
        pass
    print("finish")
if __name__ == '__main__':
  main()
