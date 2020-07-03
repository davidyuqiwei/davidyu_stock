#!/usr/bin/env python
# coding: utf-8
import stockstats
import pandas as pd
#import matplotlib.pyplot as plt
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

def process(df1,start_date,end_date,max_min_stat_window,regre_window,regre_col):
    stock = DF_to_StockDataFrame(df1)
    stock = select_data(stock,start_date,end_date)
    stock_kdj_macd = stock_kdj(stock)
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
    from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
    from functions.rolling_regression import *
    data_dir = data_dict.get("test")
    file_name = "day_history_rand.csv"
    file_in = os.path.join(data_dir,file_name)
    df1 = pd.read_csv(file_in,sep="\t").iloc[300:,:]
    df1.columns = [x.split(".")[1] for x in df1.columns.tolist()]
    #df1['close'] = df1['adj_close']
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

