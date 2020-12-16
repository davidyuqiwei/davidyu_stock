from davidyu_cfg import *
import pandas as pd
from functions.stockstats.stockStats import *



def set_buy_sell(df_stock):
    df_stock["process"][df_stock["kdjj"]<0] = "buy"
    df_stock["process"][df_stock["kdjj"]>100] = "sell"
    return df_stock

def set_buy_sell_rsi(df_stock,low_index,high_index):
    df_stock["process"][df_stock["rsi_6"]<low_index] = "buy"
    df_stock["process"][df_stock["rsi_6"]>high_index] = "sell"
    return df_stock

#df_stock1 = df_stock[["close","process"]]

def make_process_data(df1,df_stock):
    df1["process"] = df_stock["process"]
    df2 = df1[["close","process","stock_date"]]
    df3 = df2[(df2["process"]=="buy")|(df2["process"]=="sell")]
    df3["process_num"] = 1
    df3["process_num"][df3["process"]=="buy"]=-1
    #df3["process_num_diff"] = df3["process_num"].diff()
    val = []
    p2 = "no"
    for row in df3.T.iteritems():
        a1 = row[1]
        if a1["process"] =="buy" and p2 != "buy":
            val.append(a1)
        if a1["process"] =="sell" and p2 != "sell":
            val.append(a1)
        p2 = a1["process"]
    df_process = pd.DataFrame(val) 
    df_process = df_process.reset_index()
    if df_process.iloc[0,:].process== 'sell':
        df_process = df_process.drop(index=[0])
    
    df_process = df_process.reset_index()
    if df_process.iloc[df_process.shape[0]-1,:].process== 'buy':
        df_process = df_process.drop(index=[df_process.shape[0]-1])
    return df_process


def get_kdj(df1):
    df1.rename(columns={'date':'stock_date'},inplace=True)
    df1["stock_index"] = [ x[3:] for x in df1["code"].values]
    stock = DF_to_StockDataFrame(df1)
    df_stock = stock_kdj(stock)
    df_stock["process"] = "no"
    return df1,df_stock

stock_index = '601398'
data_file = "/home/davidyu/stock/data/baostock/history_data/%s.csv" %stock_index
df1 = pd.read_csv(data_file)
df1,df_stock = get_kdj(df1)
df_stock = set_buy_sell_rsi(df_stock,30,70)

df_process= make_process_data(df1,df_stock)
df_process["mm"] = df_process["close"] * df_process["process_num"]
print(df_process["mm"].sum())

r1 = df_process[df_process["stock_date"]>"2019-01-01"]["mm"].sum() 
print(r1)












