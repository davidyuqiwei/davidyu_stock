from functions import *
import os
from write_to_csv import *
import sys
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
def main():
    import sys
    sys.path.append("../..")
    from dir_control.data_dir import dir_basic_info,dir_financial_report,stk_index_list
    import time
    html_base="http://money.finance.sina.com.cn/corp/go.php/vFD_FinancialGuideLine/stockid/%s/ctrl/%s/displaytype/4.phtml"
    #sym='000917'
    year1=2017
    save_dir=dir_financial_report
    for i in stk_index_list[0:2]:
        if str(i)[0]=='3':
            pass
        elif len(str(i))<6:
            stock_index=str(i).zfill(6)
            html1=html_base %(stock_index,str(year1))
            download_table(html1,stock_index,str(year1),save_dir)
            print("sleep")
            time.sleep(5)
        elif str(i)[0]=='6':
            stock_index=str(i)
            html1=html_base %(stock_index,str(year1))
            download_table(html1,sym,str(year1),save_dir)
            print("sleep")
            time.sleep(5)
if __name__ =='__main__':
    main()
