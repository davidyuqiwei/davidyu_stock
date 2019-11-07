#from functions import *
import os
import time
import os
import sys
import pandas as pd
from davidyu_cfg import * 
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.connect_url import url_opener
def find_url(url):
    soup2=url_opener(url)
    a1=soup2.find_all(id='BalanceSheetNewTable0')
    soup1=a1[0]
    return soup1

def download_table(html,stock_index,year,save_dir):
    #print(html)
    soup1 = find_url(html)
    rows = soup1.find_all('tr')
    data = []
    for row in rows:
        cols=row.find_all('td')
        cols = [ele.text.strip() for ele in cols] ## get every data in the rows
        data.append([ele for ele in cols if ele]) ## make a list for data to save
        #print cols
    #print(data)
    data1 = pd.DataFrame(data)
    return data1
def trans_data(df):
    '''
    trans the string "--" to -9999 for save the data
    and give the column name
    '''
    df1 = df.replace("--",-9999).fillna(-9999)
    df1 = df1.T
    df1.columns = df.T.iloc[0].tolist()
    df2 = df1.iloc[1:,1:]  ## rows 1:,  columns 1:
    return df2
def main_process(stock_index,year,html_base,save_dir):
    from functions.make_dir import make_dir
    ## download data
    html1 = html_base %(stock_index,str(year))
    df = download_table(html1,stock_index,str(year),save_dir)
    #print(df)
    ### trans data
    df_tr = trans_data(df)
    df_tr['stock_index'] = stock_index
    ## save data
    dir_in = os.path.join(save_dir,stock_index)
    print(dir_in)
    make_dir(dir_in)
    file_name = os.path.join(dir_in,stock_index+'_'+str(year)+'.csv')
    df_tr.to_csv(file_name,index=0)
    return 1

def make_filename_check_if_exists(save_dir,stock_index,year):
    file_name = os.path.join(save_dir,stock_index+'_'+str(year)+'.csv')
    if_exists = os.path.exists(file_name)
    return file_name,if_exists


def do_download(stock_index,year,html_base,save_dir,file_name,if_exists):
    if (str(stock_index)[0]=='3' or if_exists == True):
        '''
        if the stock is kechuan start with '3' or if exitst then,pass
        '''
        pass
    else:
        try:
            status = main_process(stock_index,year,html_base,save_dir)
            if status == 1:
                #os.system("echo success_"+str(stock_index)+"__"+str(year)+" >> python.log")
                print("success_"+str(stock_index)+"__"+str(year)+"")
                time.sleep(2.6)
            else:
                pass
        except:
            file_name = str(stock_index)+'_'+str(year)+'.csv'
            #os.system("echo fail_"+str(stock_index)+"__"+str(year)+" >> python.log")
            print("failed_"+str(stock_index)+"__"+str(year)+"")
def main():

    #------------------ download raw table ---------------------------#
    for stock_index in stk_index_list:
        for year in year1:
            file_name = os.path.join(save_dir,stock_index+'_'+str(year)+'.csv')
            if_exists = os.path.exists(file_name)
            #os.system("echo "+str(if_exists)+str(stock_index)+"__"+str(year)+" >> python.log")
                    #print(file_name)
    print("finished task")
    #--------------- transform the data

if __name__ =='__main__':
    #main()
    #dir_fin_report = data_dict.get("test")
    dir_fin_report = data_dict.get("financial_report")
    html_base = "http://money.finance.sina.com.cn/corp/go.php/vFD_FinancialGuideLine/stockid/%s/ctrl/%s/displaytype/4.phtml"
    year1 = range(2000,2019+1)
    #from download_fin_report_v2 import *
    #year=2017
    #stock_index="000917"
    save_dir = dir_fin_report
    #main_process(stock_index,year,html_base,save_dir)
    for stock_index in stk_index_list:
        for year in year1:
            file_name,if_exists = make_filename_check_if_exists(save_dir,stock_index,year)
            do_download(stock_index,year,html_base,save_dir,file_name,if_exists)

            
