import pandas as pd
from davidyu_cfg import *
from functions.common.Regressions import *
from functions.common.dfcf_fuquan_data import *
from functions.common.TimeMake import timeFunc



if __name__ == '__main__':
    import pandas as pd
    import sys

    stock_index = sys.argv[1]
    out_file = sys.argv[2]
    window = sys.argv[3]
    out_dir = sys.argv[4]
    now_date = timeFunc.getTheDatetime().get("now_date")
    #train_end_date = timeFunc.daysAgo(now_date,14)
    #train_end_date = "1900-01-01"
    try:
        save_file = os.path.join(out_dir,out_file)
        df2 = pd.read_csv(save_file)
        rows = df2.shape[0]
        if rows<=20:
            train_end_date = "1900-01-01"
        else:
            train_end_date = timeFunc.daysAgo(now_date,14)
    except:
        train_end_date = "1900-01-01"
    df = dfcf_stock_data(stock_index)
    df = df[df["dt"]>=train_end_date]
    t1 = Regressions()
    df_roll_regression =  t1.rolling_regression(df, int(window), "dt", "close")
    df_roll_regression["days_default"] = int(window)
    df_out = df_roll_regression[["dt","stock_index","slopes","slope_num_in","days_default"]]
    save_file = os.path.join(out_dir,out_file)
    df_out.round(3).to_csv(save_file,index=0,mode='a')
    df2 = pd.read_csv(save_file)
    df2 = df2[df2["dt"]!="dt"]
    df2.drop_duplicates().round(3).to_csv(save_file,index=0)
    
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

