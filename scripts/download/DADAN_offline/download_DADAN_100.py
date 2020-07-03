'''
this script get the dadan data from web,
a near realtime run 


'''
import sys
import pandas as pd
from davidyu_cfg import *
from functions.connect_url import *
from functions.get_datetime import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist


def get_html_table(html1):
    '''
    get the table from a html
    input: html
    output:  table:   the table 
             new_table_index:  how many rows in the table

    '''
    soup2 = url_opener(html1)
    table = soup2.find_all('table')[0] # Grab the first table
    #table = html1.select('table')[0]
    new_table_index = [x for x in range(0,len(table.find_all('tr')))]
    return table,new_table_index
def table_to_DF(table,new_table_index,DF_columns):
    #DF_columns = 10  ## check the table columns numbers beforw
    new_table = pd.DataFrame(columns=range(0,DF_columns),index=new_table_index) # I know the size 
    row_marker = 0
    for row in table.find_all('tr'):
        column_marker = 0
        columns = row.find_all('td')
        for column in columns:
            new_table.iat[row_marker,column_marker] = column.get_text()
            column_marker += 1
        row_marker +=1
    new_table = new_table.dropna(axis=0) 
    return new_table
def save_the_table(new_table,dir_dadan,now_date,page):
    save_dir = os.path.join(dir_dadan,now_date)
    create_dir_if_not_exist(save_dir)
    save_file = os.path.join(save_dir,page+".csv")
    new_table.to_csv(save_file,index=0)

if __name__=='__main__':
    dir_dadan = data_dict.get("DADAN_offline")
    now_date,now_date_time = get_the_datetime()
    #now_date = '2020_06_19'
    import time
    import random
    import bs4
    #html1 = "http://app.finance.ifeng.com/hq/all_stock_bill.php"
    for i in range(1,3000):
        print("------------------------------------")
        print(i)
        try:
            html1 = "http://app.finance.ifeng.com/hq/all_stock_bill.php?page=%s&by=hq_time&order=desc&amount=100"%(str(i))
            #input2 = "wget %s  -O  dadan_offline.html"%(html1)
            #os.system(input2)
            #os.system("mv -f %s %s"%("all_stock_bill.php?page="+str(i),'dadan_offline.html'))
            #f = open('dadan_offline.html')
            #html1 = bs4.BeautifulSoup(f.read(),'html5lib')
            table,new_table_index = get_html_table(html1)
            time.sleep(30+random.uniform(0, 1))
            DF_columns = 10
            new_table = table_to_DF(table,new_table_index,DF_columns)
            new_table['date'] = now_date 
            save_the_table(new_table,dir_dadan,now_date,str(i))
        except Exception as e:
            print(e.message)
            pass




#print(new_table)


#airline.table = readHTMLTable(html1, header=T, which=1,stringsAsFactors=F)
