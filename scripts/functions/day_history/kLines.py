from functions.make_dir import *
import os
from functions.data_dir import *
import logging
import datetime
from functions.LinearReg import LinearReg
class klineDate():
    '''
    @start_date: 起始日期
    @stat_days: 历史统计日期
    @pred_days: 预测日期
    输入起始日期,历史统计日期,预测日期
    返回: 统计结束日期
    预测起始日期
    预测结束日期
    '''
    def __init__(self,start_date,stat_days,pred_days):
        self.start_date = start_date
        self.stat_days = stat_days
        self.pred_days = pred_days
    def make_date(self):
        stat_end_date =  datetime.datetime.strptime(self.start_date, '%Y-%m-%d') + \
                datetime.timedelta(days=self.stat_days)
        stat_end_date = stat_end_date.strftime("%Y-%m-%d")
        pred_start_date =  datetime.datetime.strptime(stat_end_date, '%Y-%m-%d') + \
                datetime.timedelta(days=1)
        pred_start_date = pred_start_date.strftime("%Y-%m-%d")
        pred_end_date =  datetime.datetime.strptime(stat_end_date, '%Y-%m-%d') + \
                datetime.timedelta(days=self.pred_days)
        pred_end_date = pred_end_date.strftime("%Y-%m-%d")
        return stat_end_date,pred_start_date,pred_end_date



class kLine():
    '''
    para = {
        'stat_start_date':stat_start_date,
        'stat_end_date':stat_end_date,
        'pred_start_date':pred_start_date,
        'pred_end_date':pred_end_date
        }

    '''
    def __init__(self,DF,para):
        self.test = 'test'
        self.kline_para = ["open","high","low","close"]
        self.stat_start_date = para.get('stat_start_date')
        self.stat_end_date = para.get('stat_end_date')
        self.pred_start_date = para.get('pred_start_date')
        self.pred_end_date = para.get('pred_end_date')
        ############################
        self.df1 = DF
        self.df_select = DF
        self.df_pred = ''
    def set_column_name(self):
        '''
        set the column name
        '''
        self.df1.columns = ["stock_date","high","low","open","close",
            "volume","adj_close","stock_index"]
        return self
    def data_select(self,start_date,end_date):
        '''
        select data by start end date
        '''
        df_all = self.df1
        if start_date is not None and end_date is not None:
            df_select_time = df_all[(df_all['stock_date']>=start_date)&(df_all['stock_date']<=end_date)]
            self.df_select = df_select_time
        else:
            self.df_select = self.df1
        return self
    def data_select_pred(self):
        df_all = self.df1
        df_pred = df_all[(df_all['stock_date']>=self.pred_start_date)&(df_all['stock_date']<=self.pred_end_date)]
        self.df_pred = df_pred
        return self

    def get_kline_data(self):
        df2 = self.df_select[self.kline_para+["stock_date"]]
        if self.stat_start_date is not None and self.stat_end_date is not None:
            df3 = df2[self.kline_para]
        else:
            df3 = df2[self.kline_para]
        return df3


    def linearRegPred(self):
        DF = self.data_select_pred().df_pred
        slope = LinearReg.single_linear_reg(DF,'adj_close')[0]
        return slope
