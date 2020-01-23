from davidyu_cfg import *
from functions.LinearReg import LinearReg

def rolling_regression(x,window,sort_col,reg_col):
    '''
    @param: x is a dataframe
    '''
    loop_len = x.shape[0]
    slope = []
    num_in = []
    x = x.sort_values(sort_col)
    for i in range(0,loop_len):
        st_index = i
        end_index = i+window
        try:
            df3 = x.iloc[st_index:end_index,:]
            num_in.append(df3.shape[0])
            slope1,inter = LinearReg.single_linear_reg(df3,reg_col)
            slope.append(slope1)
        except:
            slope.append(-999)
    x['slopes'] = slope
    x['slope_num_in'] = num_in
    return x
