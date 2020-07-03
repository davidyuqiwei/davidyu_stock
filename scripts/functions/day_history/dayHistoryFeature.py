class dayHistoryFeature:
    '''
    历史收盘价
    '''
    new_history_days_colname= None
    def __init__(self,new_column_name=None,df_out=None):
        self.test = 'test'
        self.new_history_days_colname = new_column_name
        self.df_out = df_out
    @staticmethod
    def setnameBefore(x):
        return "close_before_%s"%(x)
    @staticmethod
    def setnameBeforeNdays(name,days):
        """
        @param: name, the name string will set
        @param: days,   n days before of the feature
        """
        return "%s_before_%s"%(name,days)
    def new_history_days_colname(self,history_days):
        for i in range(1,history_days):
            col_name = setnameBefore(str(i))
        return col_name
    @staticmethod
    def make_history_price(df1,history_days):
        '''
        make shift days price 
        @return close1,close2,close3   -->  1day before, 2day before, 3day before
        '''
        df1 = df1.sort_values('stock_date')
        insert_cols = []
        for i in range(1,history_days+1):
            col_name = dayHistoryFeature.setnameBefore(str(i))
            df1[col_name] = df1.adj_close.shift(i)
            insert_cols.append(col_name)
        dayHistoryFeature.new_history_days_colname = insert_cols
        return df1
    @staticmethod
    def makeHistoryFeature(df1,history_days,colname):
        '''
        make shift days price 
        @param: df1, input dataframe
        @param: history_days,   history days the to make features
        @param: colname,   colname to make feature
        @return close1,close2,close3   -->  1day before, 2day before, 3day before
        '''
        df1 = df1.sort_values('stock_date')
        insert_cols = []
        column_name_list = []
        for i in range(1,history_days+1):
            col_name = dayHistoryFeature.setnameBeforeNdays(colname,str(i))
            df1[col_name] = df1[colname].shift(i)
            insert_cols.append(col_name)
        dayHistoryFeature(insert_cols,df1)
        return dayHistoryFeature(insert_cols,df1)




