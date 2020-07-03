from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import setColname
from functions.DF_process import changeStockIndex
'''
update the date in df 
raw dataframe has not cover the download date,
which cannot choose by date
@ update time 2019-11-25
'''
class DaDanAna:
    SUM_COLUMNS = ["trade_num","trade_shou"]

    def __init__(self,df):
        self.test = 'test'
        self.df = self.__process_df(df)
        self.SUM_COLUMNS = ["trade_num","trade_shou"]
        self.MAX_MIN_COLUMNS = ['trade_num_adjust']
        #self.df_out = None
        df_cnt = self.__cnt(self.df)
        self.df_out = ""
    @staticmethod
    def __process_df(df):
        df1 = df.drop_duplicates()
        df1 = df1[(df1['status']=='买盘')|(df1['status']=='卖盘')]
        df2 = changeStockIndex(df1,'stock_index')
        df2 = df2.sort_values('stock_index')
        df2['trade_stat'] = df2['status']
        df2['trade_stat'][df2['trade_stat']=='买盘']=1
        df2['trade_stat'][df2['trade_stat']=='卖盘']=-1
        df2['trade_num_adjust'] = df2['trade_num'] *df2['trade_stat'] 
        return df2
    def __status_sum(self,status):
        df_status = self.df[self.df["status"] == status]
        df4 = df_status.groupby(["stock_index","stock_name"])[self.SUM_COLUMNS].sum().reset_index()
        if status == "买盘":
            df4.columns = ["stock_index","stock_name","buy_num","buy_shou"]
        elif status == "卖盘":
            df4.columns = ["stock_index","stock_name","sale_num","sale_shou"]
        return df4
    @staticmethod
    def __cnt(df):
        df1 = df.groupby(["stock_index","stock_name"]).count().reset_index()
        df1['cnt'] = df1['price']
        #print(df1[['stock_index','cnt']].head(10))
        df_cnt = df1[['stock_index','cnt']]
        return df_cnt
    def dadan_diff_stat(self):
        #df_DADAN = df_input.drop_duplicates()
        df_buy = self.__status_sum("买盘")
        df_sale = self.__status_sum("卖盘")
        ## 
        df_merge = pd.merge(df_buy,df_sale,how='outer',on = ["stock_index","stock_name"])
        df_merge = df_merge.fillna(0)
        df_merge["buy_sale_diff"] = df_merge["buy_num"]-df_merge["sale_num"]
        df_merge["buy_sale_diff_shou"] = df_merge["buy_shou"]-df_merge["sale_shou"]
        df_merge1 = df_merge.sort_values('buy_sale_diff',ascending=False)
        #print(df_merge1)
        self.df_out = df_merge1
        return self
    def dadan_diff_stat_print(self):
        print("="*50)
        print(self.df_out[['stock_index','stock_name','buy_sale_diff']].head(50))

    def max_min(self):
        self.df_out['max_buy'] = self.df.groupby(["stock_index","stock_name"])[self.MAX_MIN_COLUMNS].max().reset_index()[self.MAX_MIN_COLUMNS]
        self.df_out['min_buy'] = self.df.groupby(["stock_index","stock_name"])[self.MAX_MIN_COLUMNS].min().reset_index()[self.MAX_MIN_COLUMNS]
        #self.df_out['max_buy'] = df4['max_buy']
        #self.df_out['min_buy'] = df4['min_buy']
        return self
    def reset_columns(self,sum_col_list):
        self.SUM_COLUMNS = sum_col_list
        return self
if __name__ =='__main__':
    now_date,now_date_time = get_the_datetime()  ## the now_date is like "2019_11_08"
    now_date = "2020_06_12"
    dir_dadan = data_dict.get("DADAN")
    data_dir = os.path.join(dir_dadan,now_date)
    print(data_dir)
    df1 = combine_csv_in_folder(data_dir)
    df1.columns = setColname().DADAN()
    #aa = DaDanAna(df1).df_out
    #aa = DaDanAna(df1).max_min().dadan_diff_stat().df_out
    #print(aa.head(10))
    
    '''
    dadan sale total money
    '''
    df_merge = DaDanAna(df1).dadan_diff_stat()
    df_merge1 = df_merge.df_out
    df_merge.dadan_diff_stat_print()
    #print(df_merge1.head(50))
    #print(df_merge1.tail(30))
    


    #df_merge2 = df_merge1[df_merge1.sale_num.isna()]   
    #df_merge3 = df_merge2.sort_values("buy_num",ascending=False)  
    #df1.to_csv("DADAN_sample.csv",index=0)
    #df_merge1.to_csv("2020_01_23.csv",index=0,encoding="utf_8_sig")
    


