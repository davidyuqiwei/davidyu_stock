import os
from davidyu_cfg import *
class mergeData:
    logging.info("load merge data script"+os.getcwd())
    def __init__(self,roll_reg_file):
        self.rollRegDF = None
        self.roll_reg_file = roll_reg_file
    @staticmethod
    def index2str(df,col=None):
        if col == None:
            col = 'stock_index'
        df['stock_index'] = [str(x).zfill(6) for x in df['stock_index'].values.tolist()]
        return df
    def mergeWithRollingReg(self,df):
        df =  mergeData.index2str(df)
        df_merge = pd.merge(self.rollRegDF,df,on=("stock_date","stock_index"))
        return df_merge
    def loadRollingReg(self):
        df2 = pd.read_csv(self.roll_reg_file)
        df2 = df2[df2['slopes']!='slopes']
        df2 = mergeData.index2str(df2)
        self.rollRegDF = df2
        return self
    @staticmethod
    def regPN(df,col):
        '''
        >=0 =1
        <= =-1
        '''
        df[col] = df[col].astype(float)
        df[col][df[col]>=0] = 1
        df[col][df[col]<0] = -1
        return df

