class dayHistoryFeatureCommon:
    '''
    历史收盘价
    '''
    new_history_days_colname= None
    def __init__(self):
        self.test = 'test'
    @staticmethod
    def setnameBefore(colname:str,days:int):
        return colname+"_before_%s"%(days)
    def new_history_days_colname(self,history_days):
        for i in range(1,history_days):
            col_name = setnameBefore(str(i))
        return col_name
    @staticmethod
    def make_history_price(df1,colname,history_days):
        '''
        make shift days price 
        @return close1,close2,close3   -->  1day before, 2day before, 3day before
        '''
        df1 = df1.sort_values('stock_date')
        insert_cols = []
        for i in range(1,history_days+1):
            col_name = dayHistoryFeatureCommon.setnameBefore(colname,str(i))
            df1[col_name] = df1[colname].shift(i)
            insert_cols.append(col_name)
        dayHistoryFeatureCommon.new_history_days_colname = insert_cols
        return df1

