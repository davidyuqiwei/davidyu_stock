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
    df_dir = data_dict.get("baostock")
    df1 = pd.read_csv(os.path.join(df_dir,stock_index+".csv"))
    df1 = df1[(df1["dt"]>=start_date)&(df1["dt"]<=end_date)]
    return df1

def mkt_data():
    sh_index_dir = data_dict.get("test")
    sh_index = pd.read_csv(os.path.join(sh_index_dir,"SH_index_data.csv"))
    df_sh_index = cleanData.cleanColName(sh_index)
    df_sh_index["dt"] = df_sh_index["stock_date"]
    return df_sh_index
def get_return(df1):
    df1 = df1.sort_values("dt")
    p1 = np.array(df1.close[1:])
    p0 = np.array(df1.close[:-1])
    logret = np.log(p1/p0)
    rate=pd.DataFrame()
    rate["logret"]=logret
    rate.index=df1['dt'][1:]
    return rate
if __name__ =='__main__':
    stock_index = sys.argv[1]
    mkt_ret = get_return(mkt_data())
    start_date = '2020-09-30'
    end_date = '2020-12-17'
    stock_ret = get_return(stock_data(stock_index,start_date,end_date))

    df = pd.merge(mkt_ret,stock_ret,left_index=True,right_index=True)
    df = df.dropna()
    x=df.iloc[:,0]
    y=df.iloc[:,1]
    beta,alpha,r_value,p_value,std_err = linregress(x,y)
    beta = np.round(beta,3)
    print("{},{}".format(stock_index,beta))
    df.to_csv(stock_index+"_beta.csv",index=0)




