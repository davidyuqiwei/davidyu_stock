from functions import *
import os
import sys
import pandas as pd
def find_url(url):
    #print html1
    soup2=url_opener(url)
    a1=soup2.find_all(id='BalanceSheetNewTable0')
    #print(a1)
    #a1=soup2.findAll('table',attrs={'class','tb_01'})
    #a1=soup2.findAll('td')
    soup1=a1[0]
    return soup1

def download_table(html,stock_index,year,save_dir):
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
    data1=pd.DataFrame(data)
    return data1
def trans_data(df):
    df1=df.replace("--",-9999).fillna(-9999)
    df1=df1.T
    df1.columns=df.T.iloc[0].tolist()
    df2=df1.iloc[1:,1:]  ## rows 1:,  columns 1:
    return df2
def main_process(stock_index,year,html_base,save_dir):
    ## download data
    stock_index=str(stock_index).zfill(6)
    html1=html_base %(stock_index,str(year))
    df=download_table(html1,stock_index,str(year),save_dir)
    ### trans data
    df_tr=trans_data(df)
    df_tr['stock_index']=stock_index
    ## save data
    file_name=os.path.join(save_dir,stock_index+'_'+str(year)+'.csv')
    df_tr.to_csv(file_name,index=0)
    return 1
def main():
    import sys
    sys.path.append("../..")
    from dir_control.data_dir import dir_basic_info,dir_financial_report,stk_index_list
    import time
    import os
    ###------------- Para -----------------------#
    html_base="http://money.finance.sina.com.cn/corp/go.php/vFD_FinancialGuideLine/stockid/%s/ctrl/%s/displaytype/4.phtml"
    year1=range(2000,2018+1)
    save_dir=dir_financial_report
    #------------------ download raw table ---------------------------#
    for stock_index in stk_index_list:
        for year in year1:
            stock_index=str(stock_index).zfill(6)
            file_name=os.path.join(save_dir,stock_index+'_'+str(year)+'.csv')
            if_exists=os.path.exists(file_name)
            #os.system("echo "+str(if_exists)+str(stock_index)+"__"+str(year)+" >> python.log")
            if (str(stock_index)[0]=='3' or if_exists == True):
                pass
            else:
                try:
                    status=main_process(stock_index,year,html_base,save_dir)
                    if status == 1:
                        os.system("echo success_"+str(stock_index)+"__"+str(year)+" >> python.log")
                        time.sleep(2.6)
                    else:
                        pass
                except:
                    file_name=str(stock_index)+'_'+str(year)+'.csv'
                    os.system("echo fail_"+str(stock_index)+"__"+str(year)+" >> python.log")
                    #print(file_name)
    print("finished task")
    '''
    os_str="cat %s/*.csv > all.csv"%(save_dir)
    print(os_str)
    os.system(os_str)
    '''
    #--------------- transform the data

if __name__ =='__main__':
    main()
