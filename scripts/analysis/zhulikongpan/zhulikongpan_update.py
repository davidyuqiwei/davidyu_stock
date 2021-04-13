from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import *


def load_history_data():
    col_in = ["stock_date","stock_index","stock_name","new_price","x1","x2",
            "x3","zhuli_1_price","zhuli_ratio","zhuli_status","zhuli_20_price","a1","a2","a3",
            "a4","a5","a6","a7","a8","a9","a10","a11"]
    df_zl_history = pd.read_csv("/home/davidyu/stock/data/tmp/zhulikongpan.csv",header=None)
    df_zl_history.columns = col_in
    df_zl_history["stock_date"] = [x[0:10] for x in df_zl_history["stock_date"].values.tolist()]
    max_date = df_zl_history["stock_date"].max()
    return df_zl_history,max_date
def ratio_mean(df_zl_history,start_date,max_date):
    # ratio mean
    df_stat = df_zl_history[(df_zl_history["stock_date"]>=start_date)&(df_zl_history["stock_date"]<=max_date)]
    df_zhuli_ratio_mean = df_stat.groupby("stock_index").mean()["zhuli_ratio"].reset_index()
    df_zhuli_ratio_mean = df_zhuli_ratio_mean.sort_values("zhuli_ratio",ascending=False)
    df_zhuli_ratio_mean.columns = ["stock_index","avg_ratio_7_days"]
    return df_zhuli_ratio_mean

def run_zhulikongpan():
    #now_date,_ = get_the_datetime()
    #datetime.datetime.strptime(now_date,"%Y-%m-%d").date()
    df_zl_history,max_date = load_history_data()
    a1 = datetime.datetime.strptime(max_date,"%Y-%m-%d").date()-datetime.timedelta(7)
    start_date = a1.strftime("%Y-%m-%d")
    #print(df_zhuli_ratio_mean)
    df_zhuli_ratio_mean = ratio_mean(df_zl_history,start_date,max_date)
    ## current ratio
    df_max_date = df_zl_history[df_zl_history["stock_date"]==max_date]
    df_max = df_max_date[["stock_index","stock_date","zhuli_ratio"]]
    df_max.columns = ["stock_index","stock_date","current_zhuli_ratio"]
    aa = pd.merge(df_max,df_zhuli_ratio_mean)
    df_out = aa.sort_values("current_zhuli_ratio",ascending=False)
    #print(df_out)
    df_out1 = df_out[df_out["current_zhuli_ratio"]>0.3]
    
    """
    merge stock name
    """
    stock_name = pd.read_csv(os.path.join(data_path,"common","stock_name.csv"))
    df_out2 = pd.merge(df_out1,stock_name)
    df_out2 = df_out2[["stock_index","stock_name","current_zhuli_ratio","avg_ratio_7_days"]]
    df_out2.round(3).to_csv("zhulikongpan.csv",index=0)
run_zhulikongpan()
