import pandas as pd
from davidyu_cfg import *
from functions.rolling_regression import *
from functions.DF_process import changeStockIndex
#file1 = "/home/davidyu/stock/data/tmp_data/stock_feature/601398.csv"

class rollRegDayHis:
    def __init__(self):
        self.test = 'test'   
    @staticmethod
    def getRollReg(file1,window=None,save_name=None):
        '''
        已过滤掉不能租window长度的数据
        '''
        logging.info("----------------- start to calculate rolling regression-------------")
        if save_name ==None:
            save_name = 'test.csv'
        df1 = pd.read_csv(file1)
        stk_list = df1['stock_index'].unique().tolist()
        data_dir = tmp_data_dict.get('stock_feature')
        save_dir = os.path.join(data_dir,"rollRegression")
        df_reg = pd.DataFrame()
        if window == None:
            window = 5
        for i in stk_list:
            print(i)
            df2 = df1[df1['stock_index']==i]
            df2 = df2[['stock_date',"adj_close"]]
            df3 = rolling_regression(df2,window,"stock_date","adj_close")
            df3 = df3[df3['slope_num_in']==window]
            save_file = os.path.join(save_dir,save_name)
            df3['stock_index'] = str(i).zfill(6)
            df_reg = df_reg.append(df3)
        df_reg = changeStockIndex(df_reg,'stock_index')
        df_reg.to_csv(save_file,index=0)
        logging.info("-------------------save data {}".format(save_dir))
        return save_file
