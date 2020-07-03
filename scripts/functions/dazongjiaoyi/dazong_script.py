from functions.make_dir import *
import os
from functions.data_dir import *
import logging
logging.basicConfig(level=logging.INFO,
    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
    filename="/home/davidyu/stock/data/tmp_py_log/pylog.log")
class dazong():
    logging.info("python script path "+os.getcwd())
    def __init__(self,now_date,DF=None):
        self.now_date = now_date
        self.df = self.loadDaZongData()
    def loadDaZongData(self):
        now_date = self.now_date
        #now_date = "2020-04-17"
        data_dir = data_dict.get("dazongjiaoyi")
        file_in = "dazongjiaoyi_%s.csv"%(now_date)
        df1 = pd.read_csv(os.path.join(data_dir,file_in))
        return df1

    def add_date(self,df):
        '''
        dataframe add now dates
        '''
        df['cal_date'] = self.now_date
        return df

    def dazong_statistics(self,df):
        '''
        statistics of dazong data
        '''
        df2 = df
        ## 当日股票大宗交易额
        df_sname = df2.groupby(["SNAME","SECUCODE"])['TVAL'].sum().reset_index().sort_values("TVAL",ascending=False)
        df_sname = self.add_date(df_sname)
        ## 当日交易所最大额
        df_BUYERNAME = df2.groupby(["BUYERNAME"])['TVAL'].sum().reset_index().sort_values("TVAL",ascending=False)
        df_BUYERNAME = self.add_date(df_BUYERNAME)
        # 当日  股票&交易所 大宗交易额
        df_sname_BUYERNAME = df2.groupby(["SNAME","BUYERNAME"])['TVAL'].sum().reset_index().sort_values("TVAL",ascending=False)
        df_sname_BUYERNAME = self.add_date(df_sname_BUYERNAME)
        return df_sname,df_BUYERNAME,df_sname_BUYERNAME
    def save_to_daily_report(self):
        report_dir = data_dict.get("daily_report")
        save_dir = os.path.join(report_dir,self.now_date)
        make_dir(save_dir)
        return save_dir
    def do_dazong_stats(self,pos=0):
        '''
        只计算折益率大于0的大宗交易
        '''
        df2 = self.df.copy(deep=True)
        df2['Zyl'] = df2['Zyl'] *100
        df_in = df2
        if pos == 1:
            df_in = df2[df2['Zyl']>0]
            logging.info("dazong zheyilv postive")
        else:
            logging.info("dazong statisics")
        df_sname,df_BUYERNAME,df_sname_BUYERNAME = self.dazong_statistics(df_in)
        return df_sname,df_BUYERNAME,df_sname_BUYERNAME

