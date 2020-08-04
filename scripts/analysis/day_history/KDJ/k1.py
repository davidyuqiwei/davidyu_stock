from davidyu_cfg import *
from functions.stockstats.stockStats import *
from functions.rolling_regression import *
from functions.day_history.adjustStockPrice import adjustStockPrice


tmp_data_path = os.path.join(data_path,"test")
file_name = "600.csv"

file_name = "/home/davidyu/stock/data/tmp_data/stock_feature/rawData/history_part0.csv"
#df1 = pd.read_csv(os.path.join(tmp_data_path,file_name),sep="\t")
df1 = pd.read_csv(file_name)
df1['close'] = df1['adj_close']

df1.columns = [x.split(".")[1] for x in df1.columns.tolist()]
df1 = adjustStockPrice.adj_stock_price(df1)


stock = DF_to_StockDataFrame(df1)

feature_list = ['kdjk','kdjd','kdjj','macdh',"rsi_6","close"]


stock["rsi_6"]

window = 3

df_stock = stock_feature(stock,feature_list)
df3 = rolling_regression(df_stock,window,"stock_date","close")

cols_to_use = df3.columns.difference(df_stock.columns)
df_merge = pd.merge(df_stock,df3[["stock_date"]+cols_to_use.tolist()],on=("stock_date"))

df_merge[df_merge["rsi_6"]>95]


df_stock = stock_kdj(stock)



def cut_list_pos_neg(seq):
	cut = 0
	seq_list = []
    try:
		for i, element in enumerate(seq):
		    if seq[i] * seq[i+1] <0:
		        seq_list.append(seq[cut:(i+1)])
		        cut = i+1
    except:
        pass
    return seq_list


def contNum_extVal(seq_list):
	days_cnt = []
	ext_val = []
	for x in seq_list:
	    if np.mean(x)>0:
	        cnt_dir = 1
	        ext_val.append(np.round(np.max(x),3))
	    else:
	        cnt_dir = -1
	        ext_val.append(np.round(np.min(x),3))
	    days_cnt.append(len(x) * cnt_dir)
    return days_cnt,ext_val

seq = df_stock["macdh"].tolist()
seq_list = cut_list_pos_neg(seq)

days_cnt,ext_val = contNum_extVal(seq_list)

macd_ext_val = pd.DataFrame(ext_val) 
macd_ext_val.to_csv("macd_ext_val.csv",index=0)



