from davidyu_cfg import *
from finquant.portfolio import build_portfolio
from functions.common.baostock import *
'''
source:   https://finquant.readthedocs.io/en/latest/quickstart.html#moving-averages

names = ['GOOG', 'AMZN', 'MCD', 'DIS']
pf = build_portfolio(names=names)

In [119]: pf.data                                                                                                                                                            
Out[119]: 
                       GOOG         AMZN         MCD         DIS
                       Date                                                        
                       1962-01-02          NaN          NaN         NaN    0.058360
                       1962-01-03          NaN          NaN         NaN    0.059143
                       1962-01-04          NaN          NaN         NaN    0.059143
                       1962-01-05          NaN          NaN         NaN    0.059339
                       1962-01-08          NaN          NaN         NaN    0.059143
                       ...                 ...          ...         ...         ...
                       2020-12-18  1731.010010  3201.649902  215.080002  172.889999
'''


df_p = pd.DataFrame()
stock_list = ["000725","600837","600036","600519","600276","601318","000333","600030","000858","002475"]
#stock_index = '601398'
start_date = '2020-01-01'
end_date = '2020-12-20'
for s1 in stock_list:
    df1 = stock_data(s1,start_date,end_date)
    df_p[s1] = df1.close.values
dates = df1.dt.values
df_p.index = dates
df_p.index.name = 'Date'

pf1 = build_portfolio(data=df_p)


