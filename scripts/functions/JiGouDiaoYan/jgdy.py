class jgdy:
    def __init__(self):
        pass
    @staticmethod
    def stockIndexCheck(x):
        ''' 
        a column similar to stock index, but nneed to clean
        e.g. df['stock_index'] = df['SCode'].apply(stockIndexCheck)
        '''
        try:
            #print(str(int(x)).zfill(6))
            return str(int(x)).zfill(6)
        except:
            pass
            return '-999999'

