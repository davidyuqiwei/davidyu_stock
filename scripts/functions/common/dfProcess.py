class dfProcess:
    @staticmethod
    def featureProcess(df,col):
        '''
        >=0 =1
        <= =-1
        '''
        df[col][df[col]>=0] = 1
        df[col][df[col]<0] = -1
        return df
