class adjustStockPrice:
    def __init__(self):
        self.test = "test"
    @staticmethod
    def adj_stock_price(df1):
        df1['open'] = df1['open']*(df1['adj_close']/df1['close'])
        df1['low'] = df1['low']*(df1['adj_close']/df1['close'])
        df1['high'] = df1['high']*(df1['adj_close']/df1['close'])
        df1['close'] = df1['adj_close']
        return df1

