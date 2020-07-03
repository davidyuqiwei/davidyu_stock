import pandas as pd
from davidyu_cfg import *
from functions.rolling_regression import *
file1 = "/home/davidyu/stock/data/tmp_data/stock_feature/601398.csv"

def rollRegDayHis:
    def __init__(self):
        
    def getRollReg(file1,window=None):
        df1 = pd.read_csv(file1)
		stk_list = df1['stock_index'].unique().tolist()
		data_dir = tmp_data_dict.get('stock_feature')
		save_dir = os.path.join(data_dir,"rollRegression")
		window = 5
		for i in stk_list:
		    print(i)
		    df2 = df1[df1['stock_index']==i]
		    df2 = df2[['stock_date',"adj_close"]]
		    df3 = rolling_regression(df2,window,"stock_date","adj_close")
		    df3 = df3[df3['slope_num_in']==window]
		    save_name = '_'.join([str(i),'rollReg',str(window)])+'.csv'
		    save_file = os.path.join(save_dir,save_name)
		    df3['stock_index'] = str(i).zfill(6)
		    df3.to_csv(save_file,index=0)
