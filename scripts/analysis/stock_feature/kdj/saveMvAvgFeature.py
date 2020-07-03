import pandas as pd
from davidyu_cfg import *
from functions.LinearReg import LinearReg
from functions.rolling_regression import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import itertools

from functions.stock_feature.mvAvg import mvAvg
from featureConfig import featureConfig

feature_dir = tmp_data_dict.get("stock_feature")
save_dir = os.path.join(feature_dir,"mvAvg")
create_dir_if_not_exist(save_dir)
mv_days = [5,10,20,30,60]

for i in range(0,20):
    raw_data_name,raw_data_file = featureConfig().rawDataInfo(i)
	raw_data_name = "history_part%s.csv"%(str(i))
	raw_file = os.path.join(feature_dir,"rawData",raw_data_name)
	df1 = pd.read_csv(raw_data_file)
    df1['close'] = df1['adj_close']
    stock = DF_to_StockDataFrame(df1)
    
	mvAvgDF = mvAvg(df1,mv_days)
	df2 = mvAvgDF.addMvAvg().df
	file_name = "mvAvg_"+raw_data_name
	df2.round(2).to_csv(os.path.join(save_dir,file_name),index=0)
feature_columns = mvAvgDF.addMvAvg().mvAvg_cols


feature_name_list = np.load("feature_columns.npy")
update_feature_list = list(set(feature_name_list.tolist()+feature_columns))
np.save("feature_columns.npy",update_feature_list)
#f=open("feature_columns.txt","a+")


#df2.to_csv()


#day_hist_df = pd.read_csv("/home/davidyu/stock/data/tmp_data/stock_feature/HistoryFeature/historyPrice_history_part0.csv")
