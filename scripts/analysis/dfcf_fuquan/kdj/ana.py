from davidyu_cfg import *
from functions.common.listProcess import *
from functions.common.dfProcess import *
from functions.common.loadModule.load_module_kdj import *

df1 = pd.read_csv("/home/davidyu/stock/data/test/dfcf_fuquan_kdj.csv")
df1 = cleanData.cleanColName(df1)


def cc(x):
    x = x.sort_values("stock_date")
    x["macd_t"] = x["macdh"]
    x = dfProcess.featureProcess(x,"macd_t")
    stock_index =  str(x.stock_index.values[0])
    a1 = continue_values_stat(x["macd_t"].values.tolist())
    a2 = pd.DataFrame(a1)
    a2["stock_index"] = stock_index
    return a2

aa = df1.groupby("stock_index").apply(lambda x:cc(x))
aa1 = aa.reset_index(drop=True)





a1=continue_values_stat(df2["macd_t"].values.tolist())



df1["macd_t"] = df1["macdh"]
df1 = dfProcess.featureProcess(df1,"macd_t")

df2 = df1[df1["slope_num_in"]==30]
#df2 = df1[(df1["slope_num_in"]==5)&(df1["stock_index"]==601398)]
df2.to_csv("/home/davidyu/stock/data/test/kdj_reg_test.csv",index=0)

'''
df2["macd_t"] = df2["macdh"]
df2 = dfProcess.featureProcess(df2,"macd_t")

a1=continue_values_stat(df2["macd_t"].values.tolist())



df2[df2["macdh"]<=-0.028]

'''


