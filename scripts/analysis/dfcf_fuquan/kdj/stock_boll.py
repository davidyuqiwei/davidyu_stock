from davidyu_cfg import *
from functions.common.loadModule.load_module_kdj import *

def load_index_300():
    df_300 = pd.read_csv("/home/davidyu/stock/data/common/index_300.txt",header=None)
    index_300 = [str(x[0]).zfill(6) for x in df_300.values.tolist()]
    return index_300

index_300 = load_index_300()




ind_list = []
boll_mean_list = []
boll_std_list = []
#stk_list = ["600519","002594"]
start_date = "2018-01-01"
end_date = "2018-12-31"
set_boll_ratio_std = 0.05
set_boll_mean = 1.1
set_continue_feature = 8
for i in index_300:
    data_file = "/home/davidyu/stock/data/history_data/dfcf_fuquan/stock_index/%s_fuquan.csv"%(i)
    df1 = pd.read_csv(data_file)
    
    stock = DF_to_StockDataFrame(df1)
    ss,tt = stock_kdj(stock)
    ss1 = ss.drop_duplicates().dropna()
    ss1["boll_ratio"] = ss1["boll_ub"]/ss1["boll_lb"]
    ss1["month"] = ss1["dt"].str[0:8]+'01'
    ss1 = ss1[(ss1["dt"]>start_date)&(ss1["dt"]<=end_date)]
    
    m1 = ss1.groupby("month")["boll_ratio"].mean()
    b_std = ss1.groupby("month")["boll_ratio"].std().reset_index()
    b_std["boll_ratio_range"] = b_std["boll_ratio"]
    b_std["boll_ratio_range"][b_std["boll_ratio"]<set_boll_ratio_std]=1
    b_std["boll_ratio_range"][b_std["boll_ratio"]>set_boll_ratio_std]=0
    
    boll_std_range = b_std["boll_ratio_range"].sum()
    boll_mean = m1.mean()
    if boll_mean < set_boll_mean and boll_std_range>set_continue_feature:
        ind_list.append(i)
        boll_mean_list.append(boll_mean)
        boll_std_list.append(boll_std_range)
    




#ss1[(ss1["dt"]>"2009-01-01")&(ss1["dt"]<="2009-02-01")]

#df3["month"] = df3["dt"].str[0:8]+'01'












