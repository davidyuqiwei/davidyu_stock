from davidyu_cfg import *
from functions.LinearReg import LinearReg

def rolling_regression(x,window):
    '''
    @param: x is a dataframe
    '''
	loop_len = x.shape[0]
	slope = []
    num_in = []
	for i in range(0,loop_len):
	    st_index = i
	    end_index = i+window
        try:
	        df3 = x.iloc[st_index:end_index,:]
            num_in.append(df3.shape[0])
	        slope1,inter = LinearReg.single_linear_reg(df3,'adj_close')
	        slope.append(slope1)
	    except:
	        slope.append(-999)
    x['slopes'] = slope
    x['slope_num_in'] = num_in
    return x
