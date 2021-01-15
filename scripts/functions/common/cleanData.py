import pandas as pd

class cleanData:

    @staticmethod
    def normCol(df,col):
        return (df[col] - df[col].min())/(df[col].max() - df[col].min())
    
    
    @staticmethod
    def changeStockIndex(df,col):
        df['stock_index'] = [str(x).zfill(6) for x in df[col].values.tolist()]
        return df
    
    
    @staticmethod
    def cleanColName(df1):
        try:
            df1.columns = [x.split(".")[1] for x in df1.columns.tolist()]
        except:
            pass
        return df1
    
    @staticmethod
    def setDt(df1):
        dt_cols = ["stock_date","dadan_dt","date"]
        df_columns = df1.columns
        for i in df_columns:
            if i in dt_cols:
                df1["dt"] = df1[i]
                break
        return df1
