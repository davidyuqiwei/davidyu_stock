import pandas as pd 

df1 = pd.read_csv("today_kdj_hs_300.csv")


def new_boll(df1):
    df1["low_boll_lb"] = df1.rolling(20)['close'].mean()-df1.rolling(20)['std'].mean()




df2 = df1[(df1["low"]<df1["boll_lb"])&(df1["dt"]>="2021-01-01")]

df1[df1.boll_lb.gt(df1.low)]

df3 = df2[["dt","stock_index","low","boll_lb","boll_ub"]] 



aa=df1[df1["stock_index"]==2] 
aa["mean_high"] = aa.rolling(20)['high'].mean() 
aa["mean_low"] = aa.rolling(20)['low'].mean() 
aa["std_high"] = aa.rolling(20)['high'].std() 
aa["std_low"] = aa.rolling(20)['low'].std() 

aa["std_close"] = aa.rolling(20)['close'].std() 
aa["std_open"] = aa.rolling(20)['open'].std() 


aa["mean_close"] = aa.rolling(20)['close'].mean() 


