from davidyu_cfg import *
from functions.stockstats.stockStats import *
from functions.rolling_regression import *
from functions.day_history.adjustStockPrice import adjustStockPrice


tmp_data_path = os.path.join(data_path,"test")

def dfIndex(file_name,feature_list):
    df1 = pd.read_csv(file_name)
    #df1['close'] = df1['adj_close']
    try:
        df1.columns = [x.split(".")[1] for x in df1.columns.tolist()]
    except:
        pass
    df1 = adjustStockPrice.adj_stock_price(df1)
    df_feature = df1.groupby("stock_index").apply(lambda x:stock_feature(DF_to_StockDataFrame(x),feature_list))
    df_feature.reset_index(drop=True, inplace=True)
    return df_feature.dropna()

def dfRollReg(df_feature,window):
    df_roll_reg = df_feature.groupby("stock_index").apply(lambda x: rolling_regression(x,window,"stock_date","close"))
    df_roll_reg.reset_index(drop=True, inplace=True)
    return df_roll_reg

dataframe_list = []
feature_list = ['kdjk','kdjd','kdjj','macdh',"rsi_6","close"]
window = 5
for i in range(0,3):
    file_name = "/home/davidyu/stock/data/tmp_data/stock_feature/rawData/history_part%s_all_price.csv" %(str(i))
    df_feature  = dfIndex(file_name,feature_list)
    df_roll_reg =  dfRollReg(df_feature,window)
    cols_to_use = df_roll_reg.columns.difference(df_feature.columns)
    df_merge = pd.merge(df_feature,df_roll_reg[["stock_date","stock_index"]+cols_to_use.tolist()],on=("stock_date","stock_index"))
    df_merge1 = df_merge[df_merge["slope_num_in"] == window]
    dataframe_list.append(df_merge1)

df_merge_all = pd.concat(dataframe_list)

tmp_data_path = os.path.join(data_path,"test")
save_file = "day_history_kdj_macd_rsi_test.csv"
save_file_name = os.path.join(tmp_data_path,save_file)
df_merge_all.to_csv(save_file_name,index=0)




