import pandas as pd
from davidyu_cfg import *
from functions.LinearReg import LinearReg
from functions.rolling_regression import *

#file1 = "/home/davidyu/stock/data/test/long_data_mv_avg.csv"
file1 = "/home/davidyu/stock/data/tmp_data/stock_feature/601398.csv"
df1 = pd.read_csv(file1,sep="\t")
df1.columns = [x.split(".")[1] for x in df1.columns.tolist()]
df2 = df1.sort_values(["stock_index","stock_date"])
sort_col = "stock_date"
df3 = df2.groupby('stock_index').apply(rolling_regression, \
        window=5,sort_col=sort_col,reg_col="adj_close")
df3[["stock_date","stock_index","adj_close","slopes","slope_num_in"]]

'''
def rolling_regression(x,window):
    @param: x is a dataframe
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

'''





