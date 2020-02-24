from davidyu_cfg import *
import pandas as pd
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.run_combine_all_csv import *

def combine_the_data():
	dir_dadan = data_dict.get("DADAN")
	df1 = combine_csv_in_folder(dir_dadan)
	#df1.to_csv("all.csv",index=0)
	df1.columns = ["stock_index","stock_name", \
	            "trade_time","price","trade_num","trade_shou", \
	            "status","price_change_rate","price_change_ratio","look","stock_date"]
	df1['stock_index'] = [ str(x).zfill(6) for x in df1.stock_index.tolist()]
	df1['day'] = [x.replace("_","-") for x in df1.stock_date.tolist()]
	tmp_dir = data_dict.get("tmp")
	df1 = df1.drop_duplicates()
	df1.to_csv(os.path.join(tmp_dir,"DADAN_sample.csv"),index=0)
def combine_the_data_raw_raw():
	dir_dadan = data_dict.get("DADAN")
	df1 = combine_csv_in_folder_raw(os.path.join(dir_dadan,"2020_01_30"))
	#df1.to_csv("all.csv",index=0)
	df1.columns = ["stock_index","stock_name", \
	            "trade_time","price","trade_num","trade_shou", \
	            "status","price_change_rate","price_change_ratio","look","stock_date"]
	df1['stock_index'] = [ str(x).zfill(6) for x in df1.stock_index.tolist()]
	df1['day'] = [x.replace("_","-") for x in df1.stock_date.tolist()]
	tmp_dir = data_dict.get("tmp")
	df1 = df1.drop_duplicates()
    return df1

df1 = combine_the_data()
tmp_dir = data_dict.get("tmp")
save_file_name = "DADAN_insert_sample.csv"
#df1 = pd.read_csv(os.path.join(tmp_dir,save_file_name))
df1 = df1.drop_duplicates()
df1 = df1[df1['day']!='test.csv']
df1.to_csv(os.path.join(tmp_dir,"DADAN_insert_sample.csv"),index=0)

