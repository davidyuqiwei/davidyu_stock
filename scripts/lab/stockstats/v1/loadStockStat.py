import stockstats
def date_trans(x):
    x1 = int(x.replace("-",""))
    return x1

def DF_to_StockDataFrame(df1):
    df1 = df1.sort_index(0)
    df1.rename(columns={'stock_date':'date'},inplace=True)
    df1.date = df1.date.apply(date_trans)
    #print(df1.head())
    stock = stockstats.StockDataFrame.retype(df1)
    #print(stock.head())
    stock['date_time'] = pd.to_datetime(stock.index,format='%Y%m%d')
    stock.index = pd.to_datetime(stock.index,format='%Y%m%d')
    return stock

def select_data(stock,start_date,end_date):
    date_select = (stock.date_time>start_date)&(stock.date_time<end_date)
    stock1 = stock[date_select]
    return stock1

def stock_kdj(stock):
    df_kdj = stock[['kdjk','kdjd','kdjj']].reset_index()
    df_kdj['stock_index'] = stock['stock_index'].tolist()
    df_kdj['stock_date'] = df_kdj['date']
    df_kdj['stock_date'] = df_kdj['stock_date'].astype(str)
    df_kdj['macd'] = stock['macd'].reset_index()['macd']
    return df_kdj
def rollingFutureMaxMin(stock,r_window):
    '''
    @ future max_min
    @param   r_window:  rolling window
    '''
    shift_num = (r_window-1)*-1
    #df2 = df1[(df1.date_time>start_date) &(df1.date_time<end_date)]   
    #df3 = df2.sort_index(ascending=False)
    close_max_name = 'close_max_'+'future_'+str(abs(shift_num))
    close_min_name = 'close_min_'+'future_'+str(abs(shift_num))
    close_mean_name = 'close_mean_'+'future_'+str(abs(shift_num))
    close_diff_max_name = 'close_diffratiomax_'+'future_'+str(abs(shift_num))
    close_diff_min_name = 'close_diffratiomin_'+'future_'+str(abs(shift_num))
    high_max_name = 'high_max_'+'future_'+str(abs(shift_num))
    high_min_name = 'high_min_'+'future_'+str(abs(shift_num))
    low_max_name = 'low_max_'+'future_'+str(abs(shift_num))
    low_min_name = 'low_min_'+'future_'+str(abs(shift_num))
    stock[close_max_name]= stock['close'].rolling(window=r_window).max().shift(shift_num)
    stock[close_min_name] = stock['close'].rolling(window=r_window).min().shift(shift_num)
    stock[close_mean_name] = stock['close'].rolling(window=r_window).mean().shift(shift_num)
    stock[close_diff_max_name ] = (stock[close_max_name] - stock['close'])/stock['close']
    stock[close_diff_min_name ] = (stock[close_min_name] - stock['close'])/stock['close']
    stock[high_max_name] = stock['high'].rolling(window=r_window).max().shift(shift_num)
    stock[high_min_name] = stock['high'].rolling(window=r_window).min().shift(shift_num)
    stock[low_max_name] = stock['low'].rolling(window=r_window).max().shift(shift_num)
    stock[low_min_name] = stock['low'].rolling(window=r_window).min().shift(shift_num)
    #df_f1 = stock[['close','close_max','close_min','close_diff_ratio']]
    out_name = ['close'] + [close_max_name,close_min_name,close_diff_max_name, 
            close_diff_min_name,high_max_name, 
            high_min_name,low_max_name,low_min_name]
    df_f1 = stock[out_name]
    return df_f1
