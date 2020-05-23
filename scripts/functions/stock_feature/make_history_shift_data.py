class make_history_shift_data:
    def __init__(self):
        #self.test = 1
        self.close_str = 'close'
        self.volume_str = 'volume'


    def make_history_shift_feature(self,df1,history_days,input_str):
        '''
        make shift days price 
        @return close1,close2,close3   -->  1day before, 2day before, 3day before
        '''
        if input_str == 'adj_close':
            col_str = self.close_str
        elif input_str == 'volume':
            col_str = self.volume_str
        else:
            pass
        for i in range(1,history_days):
            col_name = col_str+str(i)
            df1[col_name] = df1[input_str].shift(i)
        return df1
    def make_history_price(self,df1,history_days):
        '''
        make shift days price 
        @return close1,close2,close3   -->  1day before, 2day before, 3day before
        '''
        df1 = self.make_history_shift_feature(df1,history_days,'adj_close')
        return df1  
    def make_history_volume(self,df1,history_days):
        '''
        make shift days price 
        @return close1,close2,close3   -->  1day before, 2day before, 3day before
        '''
        df1 = self.make_history_shift_feature(df1,history_days,'volume')
        return df1  







"""
    def make_history_price(self,df1,history_days):
        '''
        make shift days price 
        @return close1,close2,close3   -->  1day before, 2day before, 3day before
        '''
        for i in range(1,history_days):
            col_name = self.close_str+str(i)
            df1[col_name] = df1.adj_close.shift(i)
        return df1    
    
    def make_history_vol(self,df1,history_days):
        '''
        make shift days price 
        @return close1,close2,close3   -->  1day before, 2day before, 3day before
        '''
        for i in range(1,history_days):
            col_name = self.volume_str+str(i)
            df1[col_name] = df1.volume.shift(i)
        return df1    
"""

    

