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
    def col2Float(df,columns):
        import numpy as np
        df1 = df.copy()
        for col in columns:
            df1[col] = [ np.float(x) for x in df[col].values ]
        return df1
