import pandas as pd

def stock_return(df1,col,sort_col="dt"):
    df1 = df1.sort_values(sort_col)
    df1["close"] = df1[col]
    returns = (df1.close.diff(1)/df1.close).values
    df1["daily_return"] = returns
    return df1
