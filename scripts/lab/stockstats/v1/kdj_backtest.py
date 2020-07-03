#!/usr/bin/env python
# coding: utf-8
#import heartrate,files
#from heartrate import trace, files

def nextPrice(stock,n):
    sale_columns = []
    for i in range(2,n+1):
        low_col = 'next_low_' + str(i)
        high_col = 'next_high_' + str(i)
        stock[low_col] = stock['low'].shift(-1*i).tolist()
        stock[high_col] = stock['high'].shift(-1*i).tolist()
        sale_columns.append(low_col)
        sale_columns.append(high_col)
    return stock,sale_columns

def process():
    stock = DF_to_StockDataFrame(df1)
    stock_kdj_macd = stock_kdj(stock)
    kdj_thre = 0
    buy_num = 1000
    sale_days_threshold = 5
    # 第二天用高于昨日最低价的百分之多少买入
    buy_increase_ratio = 0.01

    stock['next_low_1'] = stock['low'].shift(-1).tolist()
    stock,sale_columns = nextPrice(stock,sale_days_threshold)
    stock['stock_date'] = df1['stock_date'].astype(str).tolist()

    stock1 = stock[stock['kdjj']<kdj_thre]
    stock1['buy_price_now'] = stock1['low']*(1+ buy_increase_ratio/100)
    stock1['if_can_buy'] = stock1['buy_price_now'] - stock1['next_low_1'] 
    stock1[stock1['if_can_buy']>0].shape[0]/stock1.shape[0]
    #stock1 = stock[(stock['macd']<kdj_thre)&(stock['kdjj']<kdj_thre)]
    
    #stock1['buy_price'] = stock1['next_low_1'] * 1.005
    stock1['buy_price'] = stock1['buy_price_now']
    
    stock1['positive_price'] = stock1['buy_price'] * 1.005
    stock1['future_max'] = stock1[sale_columns].max(axis=1)
    
    stock1['max_can_sale'] =  stock1['future_max']-stock1['positive_price']
    stock1[stock1['max_can_sale']>0].shape[0]/stock1.shape[0]



    stock['buy'] = stock['kdjj']
    
    stock1 = stock[stock['kdjj']<kdj_thre]
        
    
    stock1 = stock[stock['kdjj']<20]
    a1=stock1['next_low']/stock1['close']
    a1.mean()
    a1=stock1['next_low']/stock1['low']
    a1.mean()

    from sklearn import linear_model
    from sklearn.metrics import explained_variance_score,\
            mean_absolute_error,\
            mean_squared_error,\
            median_absolute_error,r2_score
    reg = linear_model.LinearRegression(fit_intercept=True,normalize=False)
    stock1 = stock[['high','low','open','close','next_low']].dropna()
    x = stock1[['high','low','open','close']].values
    y = stock1.next_low.values
    reg.fit(x,y)

    mean_squared_error(y,reg.predict(x)) 
    r2_score(y,reg.predict(x))

    cols_to_use = stock_kdj_macd.columns.difference(stock.columns).tolist()+['stock_date']
    df_f2 = pd.merge(stock,stock_kdj_macd[cols_to_use],on="stock_date")

    #stock = select_data(stock,start_date,end_date)
    stock_kdj_macd = stock_kdj(stock)
    pd.merge(stock_kdj_macd,stock,on="stock_date")

    #kdj_feature = setFeature(df_kdj,'tes',14,['kdjk','kdjj','kdjd'])
    df_max_min = rollingFutureMaxMin(stock,max_min_stat_window)
    #df_f2 = df_f1.merge(df_kdj, left_index=True, right_index=True)
    df_max_min = df_max_min.reset_index()
    df_max_min = rolling_regression(df_max_min,regre_window,'date',regre_col)    
    #df_max_min['slope_5'] = linear_slope['slopes']
    df_max_min = df_max_min.reset_index().dropna()
    df_max_min['stock_date'] = df_max_min.reset_index()['date'].astype(str)
    ## combine data
    cols_to_use = df_max_min.columns.difference(stock_kdj_macd.columns).tolist()+['stock_date']
    df_f2 = pd.merge(stock_kdj_macd,df_max_min[cols_to_use],on="stock_date")
    return df_f2


if __name__ == "__main__":
	import stockstats
	import pandas as pd
	#import matplotlib.pyplot as plt
	from davidyu_cfg import *
	from functions.LinearReg import *
	#https://blog.csdn.net/freewebsys/article/details/78578548
	import loadStockStat
    from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
    from functions.rolling_regression import *
    data_dir = data_dict.get("test")
    file_name = "601398.csv"
    file_in = os.path.join(data_dir,file_name)
    df1 = pd.read_csv(file_in,sep="\t").iloc[300:,:]
    df1.columns = [x.split(".")[1] for x in df1.columns.tolist()]
    #df1['close'] = df1['adj_close']
    df1['open'] = df1['open']*(df1['adj_close']/df1['close'])
    df1['low'] = df1['low']*(df1['adj_close']/df1['close'])
    df1['high'] = df1['high']*(df1['adj_close']/df1['close'])
    df1['close'] = df1['adj_close']


    start_date = '2019-01-01'
    end_date = '2019-12-31'
    max_min_stat_window = 5
    regre_window = 3
    regre_col = 'close'
    df_out = []
    for name,group in df1.groupby('stock_index'):
        df2 = process(group,start_date,end_date,max_min_stat_window,regre_window,regre_col)
        df_out.append(df2)

    df_f2 = pd.concat(df_out)
    #df_f2.to_excel("test.xlsx",index=0)

"""
a1 = df_f2[["stock_index","slopes","kdjj","close","close_max_future_4","high_max_future_4","macd","low_max_future_4"]]
a2 = a1[(a1["kdjj"]<20)]

a2 = a1[(a1["macd"]<20)&(a1['kdjj']<0)]

a1['slopes'][(a1['slopes']<0.3)&a1['slopes']>-0.3].mean()
a2['slopes'][(a2['slopes']<0.3)&(a2['slopes']>-0.3)].mean()



#a2['slopes'][a2['slopes']<0.3].mean() 



a2['diff'] = (a2['low_max_future_4'] - a2['close'])/a2['close']
a2['diff'].mean() 
a2['diff'].quantile(0.5)

a2 = a1[(a1["macd"]>-100)&(a1['kdjj']<0)]
a2['diff'] = (a2['close_max_future_4'] - a2['close'])/a2['close']
a2['diff'].mean() 
a2['diff'].quantile(0.5)





a2 = a1[a1["kdjj"]<0]
a2['diff'] = (a2['close_max_future_4'] - a2['close'])/a2['close']
a2['diff'].mean() 

"""

'''
from functions.stock_feature.mergeData import mergeData

df_f2['cl_diff'] = (df_f2['close_max_future_4'] - df_f2['close'])/df_f2['close']
a1 = df_f2[['kdjk','kdjd','kdjj','macd','cl_diff']]
df_model = mergeData.regPN(df_f2,'slopes')

df_x = df_model[['kdjk','kdjd','kdjj','macd']]
df_y = df_model.slopes.values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test  = train_test_split(df_x,df_y,test_size=0.1, random_state=32)

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(random_state=0)
rfc = rfc.fit(X_train,y_train)
rfc.score(X_test,y_test)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train,y_train)


'''





'''

df2['close_max'] = df3['close'].rolling(5).max().sort_index()
df2['close_min'] = df3['close'].rolling(5).min().sort_index()

'''

# stock.set_index(['date'],inplace=True)
#stock.head(10)


#df_f2.to_csv("test.csv")


'''
#plt.plot(stock.date_time,stock.close)
#plt.plot(stock.date_time,stock['close_delta'])
stock[['volume','volume_delta']].plot(figsize=(20,10), grid=True)
plt.show()
stock[['close','close_delta']].plot(subplots=True, figsize=(20,10), grid=True)
plt.show()


# In[99]:


stock[
    ['close','close_1_d','close_2_d','close_-1_d','close_-2_d']
         ].plot(subplots=True, figsize=(20,10), grid=True)
plt.show()
# close_1_d  1 天的价差。 n天 - (n+1)天
# close_2_d  1 天的价差。 n天 - (n+2)天
# shift 函数是将数据 向前-n 向后+n 移动n天。 但是这个操作做了一个负值。
# 也就是 close_-1_d 才是和昨天的差 close_1_d 是和明天的差


# In[100]:


stock[
    ['close','cr','cr-ma1','cr-ma2','cr-ma3']
         ][300:].plot(subplots=True, figsize=(20,10), grid=True)
plt.show()
# CR跌穿a、b、c、d四条线，再由低点向上爬升160时，为短线获利的一个良机，应适当卖出股票。
# CR跌至40以下时，是建仓良机。而CR高于300~400时，应注意适当减仓


# In[106]:


stock['cr']
plt.scatter(stock['cr'],stock['close_-10_d'],s=2)


# In[130]:


# 随机指标(KDJ)一般是根据统计学的原理，通过一个特定的周期（常为9日、9周等）内出现过的最高价、
# 最低价及最后一个计算周期的收盘价及这三者之间的比例关系，来计算最后一个计算周期的未成熟随机值RSV，
# 然后根据平滑移动平均线的方法来计算K值、D值与J值，并绘成曲线图来研判股票走势。

# （3）在使用中，常有J线的指标，即3乘以K值减2乘以D值（3K－2D＝J），其目的是求出K值与D值的最大乖离程度，
# 以领先KD值找出底部和头部。J大于100时为超买，小于10时为超卖

# stock.tail(100)[['close','kdjk','kdjd','kdjj'] # 分别是k d j 三个数据统计项。
#          ].plot(subplots=True,figsize=(20,10), grid=True)
# plt.show()
date_select = (stock.date_time>'2015-01-01')&(stock.date_time<'2015-12-31')
date_select = (stock.date_time>'2019-06-01')

# print(date_select)
stock[date_select][['close']].plot(subplots=True,figsize=(20,4), grid=True)# 分别是k d j 三个数据统计项。
plt.show()
stock[date_select][['kdjk','kdjd','kdjj'] # 分别是k d j 三个数据统计项。
         ].plot(figsize=(20,4), grid=True)
plt.show()

'''

