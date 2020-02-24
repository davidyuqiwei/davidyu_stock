'''
this script get the dadan data from web,
a near realtime run # every 1mint

'''
import sys
import pandas as pd
from davidyu_cfg import *
from functions.connect_url import url_opener
from functions.get_datetime import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist


def get_html_table(html1):
    '''
    get the table from a html
    input: html
    output:  table:   the table 
             new_table_index:  how many rows in the table

    '''
#    html1 = "http://app.finance.ifeng.com/hq/all_stock_bill.php"
    soup2 = url_opener(html1)
    table = soup2.find_all('table')[0] # Grab the first table
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
def save_the_table(new_table,dir_dadan,now_date,now_date_time):
    save_dir = os.path.join(dir_dadan,now_date)
    create_dir_if_not_exist(save_dir)
    save_file = os.path.join(save_dir,now_date_time+".csv")
    new_table.to_csv(save_file,index=0)

if __name__=='__main__':
    dir_dadan = data_dict.get("DADAN")
    now_date,now_date_time = get_the_datetime()
    #html1 = "http://app.finance.ifeng.com/hq/all_stock_bill.php"
    html1 = "http://app.finance.ifeng.com/hq/all_stock_bill.php?amount=200"
    ## update to > 200w case, 
    table,new_table_index = get_html_table(html1)
    DF_columns = 10
    new_table = table_to_DF(table,new_table_index,DF_columns)
    new_table['date'] = now_date 
    save_the_table(new_table,dir_dadan,now_date,now_date_time)





#print(new_table)


#airline.table = readHTMLTable(html1, header=T, which=1,stringsAsFactors=F)
