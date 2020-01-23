#!/usr/bin/env python
# coding: utf-8
import stockstats
import pandas as pd
import matplotlib.pyplot as plt
from davidyu_cfg import *
from functions.LinearReg import *
#https://blog.csdn.net/freewebsys/article/details/78578548
#import heartrate,files
#from heartrate import trace, files

#trace(files=files.all,host='0.0.0.0')


def date_trans(x):
    x1 = int(x.replace("-",""))
    return x1


# In[96]:

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
    df_kdj = stock[['kdjk','kdjd','kdjj']]
    return df_kdj


def rolling_max_min(stock,r_window):
    '''
    @param   r_window:  rolling window
    '''
    shift_num = (r_window-1)*-1
    #df2 = df1[(df1.date_time>start_date) &(df1.date_time<end_date)]   
    #df3 = df2.sort_index(ascending=False)
    stock['close_max'] = stock['close'].rolling(window=r_window).max().shift(shift_num)
    stock['close_min'] = stock['close'].rolling(window=r_window).min().shift(shift_num)
    stock['close_diff_ratio'] = (stock['close_max'] - stock['close'])/stock['close']
    df_f1 = stock[['close','close_max','close_min','close_diff_ratio']]
    return df_f1


#stock['macd']


def rolling_linear_reg(df_f1,col_name,window):
    linear_slope = []
    #window = 5
    for i in range(0,df_f1.shape[0]):
        df_in = df_f1.iloc[i:(i+window)]
        sl = LinearReg.single_linear_reg(df_in,col_name)
        linear_slope.append(sl[0])
    return linear_slope

from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
data_dir = dir_dadan = data_dict.get("test")
file_name = "601398.csv"
file_in = os.path.join(data_dir,file_name)
df1 = pd.read_csv(file_in,sep="\t").iloc[300:,:]
df1.columns = [x.split(".")[1] for x in df1.columns.tolist()]
stock = DF_to_StockDataFrame(df1)
start_date = '2019-01-01'
end_date = '2019-12-31'
stock = select_data(stock,start_date,end_date)
df_kdj = stock_kdj(stock)
r_window = 5
df_max_min = rolling_max_min(stock,r_window)
#df_f2 = df_f1.merge(df_kdj, left_index=True, right_index=True)
col_name = 'close'
window = 5
linear_slope = rolling_linear_reg(df_max_min,col_name,window)

df_max_min['slope_5'] = linear_slope
df_f2 = df_kdj.merge(df_max_min, left_index=True, right_index=True)
df_f2['macd'] = stock['macd']
df_f2.to_excel("test.xlsx",index=0)

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

