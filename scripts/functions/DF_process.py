import pandas as pd
def norm_col(df,col):
    return (df[col] - df[col].min())/(df[col].max() - df[col].min())
def changeStockIndex(df,col):
    df['stock_index'] = [str(x).zfill(6) for x in df[col].values.tolist()]
    return df

