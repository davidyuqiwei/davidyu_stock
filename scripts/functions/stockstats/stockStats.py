# coding: utf-8
import stockstats
import pandas as pd
#import matplotlib.pyplot as plt
from davidyu_cfg import *
from functions.LinearReg import *
def date_trans(x):
    x1 = int(x.replace("-",""))
    return x1

def DF_to_StockDataFrame(df1):
    df1 = df1.sort_values('stock_date')
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
    df_kdj['macdh'] = stock['macdh'].reset_index()['macdh']
    return df_kdj

def stock_feature(stock,feature_list):
    df_kdj = stock[feature_list].reset_index()
    df_kdj['stock_index'] = stock['stock_index'].tolist()
    df_kdj['stock_date'] = df_kdj['date'].astype(str)
    return df_kdj


