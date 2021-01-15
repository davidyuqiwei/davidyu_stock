import pandas as pd
from davidyu_cfg import *
from functions.common.Regressions import *


if __name__ == '__main__':
    import pandas as pd
    import sys

    input_file = sys.argv[1]
    input_dir = "/home/davidyu/stock/data/dfcf_fuquan/parse_data"
    out_file = sys.argv[2]
    out_dir = "/home/davidyu/stock/data/feature_center/rolling_regression/stock_index"
    window = sys.argv[3]
    df = pd.read_csv(os.path.join(input_dir,input_file))
    t1 = Regressions()
    df_roll_regression =  t1.rolling_regression(df, int(window), "dt", "close")
    df_roll_regression["days_default"] = int(window)
    df_out = df_roll_regression[["dt","stock_index","slopes","slope_num_in","days_default"]]
    df_out.round(3).to_csv(os.path.join(out_dir,out_file),index=0)
    
    
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

