
from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import *


input_file = "jijin_data.csv"
data_dir = tmp_data_dict.get("baostock")

data_file = os.path.join(data_dir,"feature_slope",input_file)
df1 = pd.read_csv(data_file,header=None)
## dadan col
#df1.columns = ["stock_index","stock_date","dadan_money"]

# jijin col
df1.columns = ["stock_index","stock_date","stock_name","jijin_nums"]

p_days_list = [30,60,90]

for i in range(0,df1.shape[0]):
    for p_days in p_days_list:
    	stock_index = str(df1["stock_index"][i]).zfill(6)
    	start_date = str(df1["stock_date"][i])
    	pred_days = str(p_days)
    	os.system("python stock_slope.py %s %s %s" %(stock_index,start_date,pred_days))




