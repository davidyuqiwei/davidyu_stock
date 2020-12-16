from davidyu_cfg import *
from functions.stockstats.stockStats import *
from loadData import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist,tmp_data_dict


stockstats.StockDataFrame.KDJ_WINDOW=9
stock = DF_to_StockDataFrame(df_stock)
#stock["kdjk"]

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
feature_list = ['kdjk','kdjd','kdjj','macdh','rsi_6','wr_6','wr_10','wr_20',
    'rsi_12','rsi_24']


all_feature = new_rsi+new_wr+feature_list+new_col_list
all_feature = list(set(all_feature))
np.save("all_feature.npy",all_feature)
df_kdj = stock[all_feature].reset_index()
df_kdj['stock_date'] = df_kdj['date'].astype(str)

df_kdj = df_kdj.dropna()
df_kdj = df_kdj[["stock_date"]+all_feature]
save_dir = tmp_data_dict.get("SH_index")
df_kdj.round(3).to_csv(os.path.join(save_dir,"sh_index_kdj.csv"),index=0)



