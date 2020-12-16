class Regressions:
    @staticmethod
    def single_linear_reg(df, column_in, if_normed=1):
        """
        linear regression for one column
        x: 0: length(y)
        y: y
        """
        import pandas as pd
        from sklearn.linear_model import LinearRegression
        from sklearn import linear_model
        import numpy as np
        X_in1 = pd.DataFrame(df, columns=[column_in])
        X = pd.DataFrame(X_in1, columns=[column_in]).dropna()
        # how many rows in the dataframe and make it as x
        rows = X.shape[0]
        x = np.array(range(rows)).reshape(-1, 1)
        if if_normed == 1:
            y = X.values
            y_normed = (y - y.min(axis=0)) / (y.max(axis=0) - y.min(axis=0) + 0.001)
        else:
            y_normed = X.values
        # regression
        regr = linear_model.LinearRegression()
        regr.fit(x, y_normed)
        slope = round(regr.coef_.item(), 5)
        inter = round(regr.intercept_.item(), 2)
        return slope, inter

    @classmethod
    def rolling_regression(cls, x, window, sort_col, reg_col):
        """
        :param x: x is a dataframe
        :param window: regression window
        :param sort_col: which column sort the DF: e.g. stock_date
        :param reg_col: which column need to do regression:  e.g. adj_close
        :return:
        """
        loop_len = x.shape[0]
        slope = []
        num_in = []
        x = x.sort_values(sort_col)
        for i in range(0, loop_len):
            st_index = i
            end_index = i + window
            try:
                df3 = x.iloc[st_index:end_index, :]
                num_in.append(df3.shape[0])
                slope1, inter = Regressions.single_linear_reg(df3, reg_col)
                slope.append(slope1)
            except:
                slope.append(-999)
        x['slopes'] = slope
        x['slope_num_in'] = num_in
        return x
    @staticmethod
    def getSlope(DF,start_date,stat_days,pred_days,col):
        df1 = cleanData.cleanColName(DF)
        df1 = cleanData.setDt(df1)
        df_columns = df1.columns
        if col not in df_columns:
            logging.error("no input slope columns: "+col)
            sys.exit(1)
        try:
            k1 = klineDate(start_date,stat_days,pred_days)
            stat_end_date,pred_start_date,pred_end_date = k1.make_date()
            df2 = df1[(df1["dt"]>=pred_start_date)&(df1["dt"]<=pred_end_date)]
            slope = LinearReg.single_linear_reg(df2,col)[0]
        except:
            slope = -999
            pred_start_date = -999
            pred_end_date = -999
        return slope,pred_start_date,pred_end_date




if __name__ == '__main__':
    import pandas as pd
    # from scripts.functions.common.Regressions import *
    d = {'col1': [1, 2, 5, 12, 4, 3, 1, 1, 2, 3, 8], 'col2': [1, 2, 5, 12, 4, 3, 11, 1, 2, 12, 3]}
    df = pd.DataFrame(data=d)
    # t1 = Regressions()
    # slope, inter = t1.single_linear_reg("col1")
    # print("slope " + str(slope))
    # print("intercept " + str(inter))
    t1 = Regressions()
    x = t1.rolling_regression(df, 4, "col2", "col1")
    print(x)

