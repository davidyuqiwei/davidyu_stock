import pandas as pd
import json
from davidyu_cfg import *
from functions.common.parseToDF import *



history_data_dir = "/home/davidyu/stock/data/history_data/dfcf_fuquan/stock_index"
new_data_dir = os.path.join(data_dict.get("dfcf_fuquan"),"parse_data")
hist_file = os.listdir(history_data_dir)
for f1 in hist_file:
    try:
	    new_data = pd.read_csv(os.path.join(new_data_dir,f1))
	    history_file = os.path.join(history_data_dir,f1)
	    history_data = pd.read_csv(history_file)
	    history_data = history_data[~history_data["dt"].isin(new_data["dt"])]

	    all_data = pd.concat([new_data,history_data]).drop_duplicates().sort_values("dt")
	    all_data.to_csv(history_file,index=0)
    except:
        pass
