import pandas as pd
from davidyu_cfg import *
from functions.common.Regressions import *


if __name__ == '__main__':
    import pandas as pd
    import sys

    input_file = sys.argv[1]
    out_file = sys.argv[2]
    df = pd.read_csv(input_file,header=None)
    df.columns = ["stock_index","close","dt"]
    df = df.sort_values("dt")
    t1 = Regressions()
    df_roll_regression = t1.rolling_regression(df, 5, "stock_index", "close")
    df_roll_regression.to_csv(out_file,index=0)
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

