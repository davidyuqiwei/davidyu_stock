from davidyu_cfg import *
import stockstats
from functions.stockstats.stockStats import *

def addNewFeature(df_stock):
    df_raw_col = df_stock.columns.tolist()
    stock = DF_to_StockDataFrame(df_stock)
    new_col_list = []
    for i in range(5,20):
        stockstats.StockDataFrame.KDJ_WINDOW=i
        stock1 = DF_to_StockDataFrame(df_stock)
        new_col1 = "kdjk_"+str(i)
        new_col2 = "kdjd_"+str(i)
        new_col3 = "kdjj_"+str(i)
        stock[new_col1] = stock1["kdjk"]
        stock[new_col2] = stock1["kdjd"]
        stock[new_col3] = stock1["kdjj"]
        add_list = [new_col1,new_col2,new_col3]
        new_col_list = new_col_list + add_list
    new_rsi = []
    new_wr = []
    for i in range(5,30):
        new_rsi.append("rsi_"+str(i))
        new_wr.append("wr_"+str(i))
    feature_list = ['kdjk','kdjd','kdjj','macdh','cci']
    all_feature = new_rsi+new_wr+feature_list+new_col_list
    all_feature = list(set(all_feature))
    df_out = stock[all_feature].reset_index()
    return df_out,all_feature

if __name__ == "__main__":
    data_dir = "/home/davidyu/stock/data/test/for_lstm"
    file_name = "SH_index_price_mv_avg_v2.csv"
    df1 = pd.read_csv(os.path.join(data_dir,file_name))
    df1.columns = [x.split(".")[1] for x in df1.columns.tolist()]  
    df2,all_feature = addNewFeature(df1)
    print(df2.columns.tolist())
