import pandas as pd
class mvAvg:
    def __init__(self,df,mv_days=None):
        if mv_days == None:
            self.mv_days = [5,10,20,30]
        else:
            self.mv_days = mv_days
        self.df = df
        self.mvAvg_cols = ""
    def addMvAvg(self):
        mvAvg_cols = []
        '''
        add moving average of a data frame
        '''
        mv_days = self.mv_days
        for i in mv_days:
            cols = 'mv'+str(i)
            self.df[cols] = self.df.groupby('stock_index')['adj_close'].rolling(i, min_periods=i).mean().reset_index()['adj_close']
            mvAvg_cols.append(cols)
        self.mvAvg_cols = mvAvg_cols
        return self



if __name__ == "__main__":
    file1 = "/home/davidyu/stock/data/tmp_data/stock_feature/601398.csv"
    df_raw = pd.read_csv(file1).sort_values(["stock_index","stock_date"]).head(1000)
    #mvAvg(df_raw).addMvAvg()
    print(mvAvg(df_raw).addMvAvg().mvAvg_cols)

