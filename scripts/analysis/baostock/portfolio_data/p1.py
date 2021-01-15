from davidyu_cfg import *
from functions.data_dir import *
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import *
from functions.day_history.kLines import klineDate
from functions.LinearReg import *
from functions.common.dfProcess import *
from functions.common.loadModule.load_module_kdj import *
from scipy.stats import linregress




def stock_data(stock_index,start_date,end_date):
    df_dir = os.path.join(data_path,"history_data","baostock","2020-12-17")
    df1 = pd.read_csv(os.path.join(df_dir,stock_index+".csv"))
    df1 = df1[(df1["dt"]>=start_date)&(df1["dt"]<=end_date)]
    df1 = df1.drop_duplicates()
    df1 = df1.sort_values("date")
    df1["stock_index"] = [ x[3:9] for x in df1["code"]]
    return df1

#stock_list = ["601888","600887","600519","603288","300498","000333","000651","002027","002714","000858"]
#stock_list = ["000725","600837","600036","600519","600276","601318","000333","600030","000858","002475"]
stock_list = ["000725","600837","600036","600519","600276","601318","000333","600030","000917","002475"]
df_out = pd.DataFrame()
start_date = '2020-06-30'
end_date = '2020-12-05'
for s1 in stock_list:
    df1 = stock_data(s1,start_date,end_date)
    #print(df1.head(10))
    df_out[s1] = (df1.close.diff(1)/df1.close).values
df_out["row_sum"] = df_out.apply(lambda x: x.sum(), axis=1)
df_out["dates"] = df1["date"].values
df_out1 = df_out.dropna()
#print(df_out1)
df_out1.round(3).to_csv("portf_v2.csv",index=0)



