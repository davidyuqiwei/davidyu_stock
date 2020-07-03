import sys
import pandas as pd
from davidyu_cfg import *
from functions.connect_url import url_opener
from functions.get_datetime import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.colNames import *

class dadanSina:
    def __init__(self,df):
        self.test = 'test'
    @staticmethod
    def get_html_table(url1):
        '''
        return: the html table, and how many rows in the table
        '''
        soup2 = url_opener(url1)
        table = soup2.find_all('tbody')[1]
        new_table_index = [x for x in range(0,len(table.find_all('tr')))]
        return table,new_table_index
    @staticmethod
    def table_to_DF(table,new_table_index,DF_columns):
        '''
        the soup table to DF
        '''
        new_table = pd.DataFrame(columns=range(0,DF_columns),index=new_table_index)
        row_marker = 0
        for row in table.find_all('tr'):
            column_marker = 0
            columns = row.find_all('th') + row.find_all('td')
            for column in columns:
                try:
                    new_table.iat[row_marker,column_marker] = column.get_text().encode("latin1").decode("gbk").strip()
                except:
                    new_table.iat[row_marker,column_marker] = column.get_text().strip()
                column_marker += 1
            row_marker += 1
        new_table = new_table.dropna(axis=0)
        return new_table
    @staticmethod
    def save_the_table(new_table,dir_dadan,now_date,now_date_time):
        #save_dir = os.path.join(dir_dadan,now_date)
        save_dir = dir_dadan
        create_dir_if_not_exist(save_dir)
        save_file = os.path.join(save_dir,now_date_time+".csv")
        new_table.to_csv(save_file,index=0)
    @staticmethod
    def columnToFloat(df,columns):
        """
        @param: df: a dataframe
        @param: columns: a list of the colnames that need trans to float
        """
        for col in columns:
            df[col] = df[col].apply(lambda x:x.replace(",","").replace("%","")).astype(float)
        return df
    @staticmethod
    def dfColumnsToFloat(df): 
        new_table = dadanSina.columnToFloat(df,["total_trade_vol","total_trade_vol_ratio", \
                "total_trade_money","total_trade_money_ratio", \
                "avg_price","zhuli_buy_vol","zhongxing_vol","zhuli_sale_vol"])
        return new_table
if __name__=='__main__':
    from functions.dadan_sina.dadanSina import dadanSina
    dir_dadan = data_dict.get("dadan_sina_offline")
    now_date,now_date_time = get_the_datetime()
    url1 = "http://vip.stock.finance.sina.com.cn/quotes_service/view/cn_bill_sum.php?num=100000&page=1&sort=totalvolpct&asc=0&volume=40000&type=0&dpc=1"
    DF_columns = 11
    table,new_table_index = dadanSina.get_html_table(url1)
    new_table = dadanSina.table_to_DF(table,new_table_index,DF_columns)
    new_table.columns = setColname().dadan_sina()
    new_table['date_time'] = now_date_time
    new_table['stock_date'] = now_date
    new_table = dadanSina.dfColumnsToFloat(new_table)
    dadanSina.save_the_table(new_table,dir_dadan,now_date,now_date_time)



