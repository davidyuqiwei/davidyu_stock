import pandas as pd
from davidyu_cfg import *
from functions.common.Regressions import *
from functions.common.dfcf_fuquan_data import *
import random
# load historical data
import numpy as np
#sample_rows = random.sample([x for x in range(0,df_list_all.shape[0])],500)
def list_col_to_float(col):
    a1 = col.replace("[","").replace("]","").replace(" ","").split(",")
    a2 = [np.float(x) for x in a1]
    return a2

df_list_all = pd.read_csv("similar_trend_sample_data.csv")
sample_rows = random.sample([x for x in range(0,df_list_all.shape[0])],200)
t1 = Regressions()
corr_list = []
index1 = []
index2 = []
future_corr_list = []
stock_index1 = []
stock_index2 = []
reg_list = []
#sample_rows = random.sample([x for x in range(0,df_list_all.shape[0])],500)
for i in sample_rows:
    logging.info(i)
    for j in range(0,df_list_all.shape[0]):
        a1 = list_col_to_float(df_list_all["curr_trend"].iloc[i])
        a2 = list_col_to_float(df_list_all["curr_trend"].iloc[j])
        try:
            corr_index = round(np.corrcoef(a1,a2)[0,1],2)
        except:
            corr_index = -999
        if corr_index > 0.95:
            d = {'curr_trend':a1}
            df_reg = pd.DataFrame(data=d)
            slope,integer = t1.single_linear_reg(df_reg,"curr_trend")
            try:
                f_a1 = list_col_to_float(df_list_all["future_trend"].iloc[i])
                f_a2 = list_col_to_float(df_list_all["future_trend"].iloc[j])
                corr_future_index = round(np.corrcoef(f_a1,f_a2)[0,1],2)
            except:
                corr_future_index = -999
            future_corr_list.append(corr_future_index)
            corr_list.append(corr_index)
            index1.append(df_list_all["curr_dt"][i])
            index2.append(df_list_all["curr_dt"][j])
            stock_index1.append(df_list_all["stock_index"].iloc[i])
            stock_index2.append(df_list_all["stock_index"].iloc[j])
            reg_list.append(slope)


c = { "corr_list":corr_list,
        "future_corr_list":future_corr_list,
        "curr_slope": reg_list,
        "stock_index1":stock_index1,
        "stock_index2":stock_index2,
        "curr_date_index1":index1,
        "curr_date_index2":index2
    }
df_a1 = pd.DataFrame(c)
df_a2=df_a1[df_a1["corr_list"]!=1]

df_a2.dropna().sort_values("corr_list").to_csv("out.csv",index=0)


