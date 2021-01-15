from davidyu_cfg import *
from functions.common.listProcess import *
from functions.common.dfProcess import *
df1 = pd.read_csv("/home/davidyu/stock/data/test/dfcf_fuquan_kdj_reg.csv",sep="\t")
df2 = df1[df1["slope_num_in"]==30]
#df2 = df1[(df1["slope_num_in"]==5)&(df1["stock_index"]==601398)]
df2.to_csv("/home/davidyu/stock/data/test/kdj_reg_test.csv",index=0)

'''
df2["macd_t"] = df2["macdh"]
df2 = dfProcess.featureProcess(df2,"macd_t")

a1=continue_values_stat(df2["macd_t"].values.tolist())



df2[df2["macdh"]<=-0.028]

'''


