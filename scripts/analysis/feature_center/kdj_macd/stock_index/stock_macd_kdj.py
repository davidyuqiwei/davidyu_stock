import pandas as pd
from davidyu_cfg import *
from functions.common.Regressions import *
from functions.common.dfcf_fuquan_data import *
from functions.common.macd_kdj.get_kdj import *
import talib


if __name__ == '__main__':
    import pandas as pd
    import sys

    #stock_index = "601398"
    stock_index = sys.argv[1]
    out_file = sys.argv[2]
    #window = sys.argv[3]
    out_dir = sys.argv[3]
    try:
        df = dfcf_stock_data(stock_index)
        df3 = df.groupby("stock_index").apply(lambda x: kdj_x(x)).reset_index(drop=True)
        df3 = df3.groupby("stock_index").apply(lambda x: new_kdj(x,16,3,3)).reset_index(drop=True)
        df3 = df3.groupby("stock_index").apply(lambda x: new_macd(x,'close',5,35,5)).reset_index(drop=True)
        df3["boll_ratio"] = df3["boll_ub"]/df3["boll_lb"]
        df3["macdh_mvavg5"] = df3["macdh"].rolling(5).mean()
        df3["sar"] = talib.SAR(df3.high, df3.low)
        index_para = ['turnover_rate',
           'macdh', 'cci', 'rsi_6', 'rsi_12', 'rsi_24', 'kdjk', 'kdjd', 'kdjj',
           'boll_ub', 'boll_lb', 'macd', 'macds', 'wr_6', 'wr_10', 'K', 'K_16_3_3',
           'D', 'D_16_3_3', 'J_16_3_3', 'macd_5_35_5', 'macds_5_35_5',
           'macdh_5_35_5', 'boll_ratio', 'macdh_mvavg5','sar']
        #print(df3)
        df_out = df3.drop_duplicates()
        df_out.round(3).to_csv(os.path.join(out_dir,out_file),index=0)
    except Exception as e:
        print(e)
        print(stock_index)
    
    #print(x)
    """
    d = {'col1': [1, 2, 5, 12, 4, 3, 1, 1, 2, 3, 8], 'col2': [1, 2, 5, 12, 4, 3, 11, 1, 2, 12, 3]}
    df = pd.DataFrame(data=d)
    # t1 = Regressions()
    # slope, inter = t1.single_linear_reg("col1")
    # print("slope " + str(slope))
    # print("intercept " + str(inter))
    t1 = Regressions()
    x = t1.rolling_regression(df, 4, "col2", "col1")
    print(x)

    """

