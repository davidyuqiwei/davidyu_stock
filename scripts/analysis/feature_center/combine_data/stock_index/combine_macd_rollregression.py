import pandas as pd
from davidyu_cfg import *
from functions.rolling_regression import *
from functions.stock_feature.mergeData import mergeData


def combine_data(stock_index,roll_regression_window):
	save_dir = os.path.join(data_dict.get("feature_center"),"combine_data")
	save_file = os.path.join( save_dir,stock_index+"_macd_slope"+str(roll_regression_window)+".csv")
	
	file_macd = "/home/davidyu/stock/data/feature_center/macd/stock_index/%s_macd.csv"%stock_index
	if int(roll_regression_window) == 5:
	    file_reg = "/home/davidyu/stock/data/feature_center/rolling_regression/stock_index/5days/%s_roll_reg_5.csv"%stock_index
	if int(roll_regression_window) == 3:
	    file_reg = "/home/davidyu/stock/data/feature_center/rolling_regression/stock_index/3days/%s_roll_reg_3.csv"%stock_index
	
	df_macd = pd.read_csv(file_macd)
	df_roll_reg = pd.read_csv(file_reg)
	
	a1 = pd.merge(df_roll_reg,df_macd,on=["dt","stock_index"], how='inner')
	#a2 = a1[a1["slope_num_in"]==roll_regression_window]
	a1.round(3).to_csv(save_file,index=0)
    
if __name__ == "__main__":
    stock_index = sys.argv[1]
    roll_regression_window = sys.argv[2]
    combine_data(stock_index,roll_regression_window)

    
