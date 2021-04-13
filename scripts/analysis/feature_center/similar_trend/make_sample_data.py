import pandas as pd
from davidyu_cfg import *
from functions.common.Regressions import *
from functions.common.dfcf_fuquan_data import *
import random
# load historical data
import numpy as np
def get_cut_sample(stock_index,start_date,sample_n,observe_days=7,future_observe_days=7):
    df = dfcf_stock_data(stock_index)
    df1 = df[df["dt"]>=start_date].sort_values("dt")
    rows = df1.shape[0]
    # sample rows to select
    end_rows = rows - observe_days - future_observe_days-2
    #
    sample_rows = random.sample([x for x in range(0,end_rows)],sample_n)
    close1 = df1["close"].values.tolist()
    dts = df1["dt"].values.tolist()
    
    close1_list = []
    dt_list = []
    stock_index_list = []
    future_trend_list = []
    future_dt_list = []
    for i in sample_rows:
        # observe trend & future trend
        list1 = close1[i:(i+observe_days)]
        future_trend = close1[(i+observe_days+1):(i+observe_days+future_observe_days)]
        #
        future_trend_list.append(future_trend)
        close1_list.append(list1)
        dt_list.append(dts[i])
        future_dt_list.append(dts[i+9])
        stock_index_list.append(stock_index)
    
    df_all = pd.DataFrame([stock_index_list,dt_list,close1_list,future_dt_list,future_trend_list]).T
    return df_all
if __name__ =='__main__':
    """
    make sample observe trend and future trend
    """
    
    #stock_index="601398"
    start_date = "2018-01-01"
    sample_n = 100
    # load HS 300 data
    stock_lists = pd.read_csv("/home/davidyu/stock/data/common/index_300_raw.txt",header=None)
    stock_lists.columns = ["stock_index"]                                                                                                                               
    
    test_list = [str(x).zfill(6) for x in stock_lists["stock_index"].values.tolist()]
    
    df_list = []
    for stock_index in test_list:
        try:
            df_all = get_cut_sample(stock_index,start_date,sample_n,90,30)
            df_list.append(df_all)
        except:
            pass 
    df_list_all = pd.concat(df_list)
    df_list_all.columns = ["stock_index","curr_dt","curr_trend","future_dt","future_trend"]
    df_list_all.to_csv("similar_trend_sample_data.csv",index=0)
'''

t1 = Regressions()
corr_list = []
index1 = []
index2 = []
future_corr_list = []
stock_index1 = []
stock_index2 = []
reg_list = []
sample_rows = random.sample([x for x in range(0,df_list_all.shape[0])],500)
for i in sample_rows:
    for j in range(0,df_list_all.shape[0]):
        a1 = df_list_all["curr_trend"].iloc[i]
        a2 = df_list_all["curr_trend"].iloc[j]
        d = {'curr_trend':a1}
        df_reg = pd.DataFrame(data=d)
        slope,integer = t1.single_linear_reg(df_reg,"curr_trend")
        try:
            corr_index = round(np.corrcoef(a1,a2)[0,1],2)
        except:
            corr_index = -999
        if corr_index > 0.95:
            try:
                corr_future_index = round(np.corrcoef(df_list_all["future_trend"].iloc[i],df_list_all["future_trend"].iloc[j])[0,1],2)
            except:
                corr_future_index = -999
            future_corr_list.append(corr_future_index)
            corr_list.append(corr_index)
            index1.append(i)
            index2.append(j)
            stock_index1.append(df_list_all["stock_index"].iloc[i])
            stock_index2.append(df_list_all["stock_index"].iloc[j])
            reg_list.append(slope)


c = { "corr_list":corr_list,
        "future_corr_list":future_corr_list,
        "curr_slope": reg_list,
        "stock_index1":stock_index1,
        "stock_index2":stock_index2,
        "index1":index1,
        "index2":index2
    }
df_a1 = pd.DataFrame(c)
df_a2=df_a1[df_a1["corr_list"]!=1]

df_a2.dropna().sort_values("corr_list").to_csv("out.csv",index=0)

'''

