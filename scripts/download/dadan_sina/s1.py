
import sys
import pandas as pd
from davidyu_cfg import *
from functions.connect_url import url_opener
from functions.get_datetime import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist

def get_html_table(url1):
	soup2 = url_opener(url1)
	table = soup2.find_all('tbody')[1]
	new_table_index = [x for x in range(0,len(table.find_all('tr')))]
    return table,new_table_index


def table_to_DF(table,new_table_index,DF_columns):
	new_table = pd.DataFrame(columns=range(0,DF_columns),index=new_table_index)
	row_marker = 0
	for row in table.find_all('tr'):
	    column_marker = 0
	    columns = row.find_all('th') + row.find_all('td')
	    for column in columns:
	        try:
	            new_table.iat[row_marker,column_marker] = column.get_text().encode("latin1").decode("gbk").strip()
	        except:
	             new_table.iat[row_marker,column_marker] = column.get_text()
	        column_marker += 1
	    row_marker += 1
	new_table = new_table.dropna(axis=0)
    return new_table

def save_the_table(new_table,dir_dadan,now_date,now_date_time):
    save_dir = os.path.join(dir_dadan,now_date)
    create_dir_if_not_exist(save_dir)
    save_file = os.path.join(save_dir,now_date_time+".csv")
    new_table.to_csv(save_file,index=0)

if __name__=='__main__':
    dir_dadan = data_dict.get("dadan_sina")
    now_date,now_date_time = get_the_datetime()
    url1 = "http://vip.stock.finance.sina.com.cn/quotes_service/view/cn_bill_sum.php?num=5000&page=1&sort=totalvolpct&asc=0&volume=40000&type=0&dpc=1"
    table,new_table_index = get_html_table(url1)
    DF_columns = 11
    new_table = table_to_DF(table,new_table_index,DF_columns)
    new_table.columns = ["stock_name","stock_index","detail","total_trade_vol","total_trade_vol_ratio","total_trade_money","total_trade_money_ratio","avg_price","zhuli_buy_vol","zhongxin_vol","zhuli_sale"]
    new_table['date_time'] = now_date_time
    new_table['stock_date'] = now_date
    save_the_table(new_table,dir_dadan,now_date,now_date_time)
