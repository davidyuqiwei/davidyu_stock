import pandas as pd
def norm_col(df,col):
    return (df[col] - df[col].min())/(df[col].max() - df[col].min())
