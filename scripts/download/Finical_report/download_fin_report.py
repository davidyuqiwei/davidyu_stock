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
def main():
    import sys
    sys.path.append("../..")
    from dir_control.data_dir import dir_basic_info,dir_financial_report,stk_index_list
    import time
    ###------------- Para -----------------------#
    html_base="http://money.finance.sina.com.cn/corp/go.php/vFD_FinancialGuideLine/stockid/%s/ctrl/%s/displaytype/4.phtml"
    year1=range(2014,2018+1)
    save_dir=dir_financial_report
    #------------------ download raw table ---------------------------#
    for stock_index in stk_index_list:
        for year in range(2000,2018+1):
            if str(stock_index)[0]=='3':
                pass
            else:
                try:
                    main_process(stock_index,year,html_base,save_dir)
                    time.sleep(5)
                except:
                    file_name=str(stock_index)+'_'+str(year)+'.csv'
                    print(file_name)
            '''
            df_final=trans_data(df)
            ## save data
            myfile=os.path.join(save_dir,i+'_'+str(year)+'.csv')
            #myfile_tr=os.path.join(save_dir,i+'_'+str(year)+'_tr.csv')
            df2.to_csv(myfile,index=1,columns=None,header=None)
            #write_to_csv(myfile,data)
            print("sleep")
'''
    #--------------- transform the data

if __name__ =='__main__':
    main()
    '''
    myfile=os.path.join(save_dir,stock_index+'_'+year+'.csv')
    myfile_tr=os.path.join(save_dir,stock_index+'_'+year+'_tr.csv')
    #write_to_csv(myfile,data)
    #os.system("sed -i '1d' "+myfile)  ## remove the first line, which is blank
    #os.system("sed -i '2d' "+myfile)  ## remove the second line
    #os.system('iconv -f utf-8 -t GB2312 %s > %s' %(myfile,myfile_tr))
    #os.system('iconv -f -t GB2312 -t utf-8 %s > %s' %(myfile,myfile_tr))
    print(myfile)
    #os.system('mv *.csv '+move_dir)
    '''
