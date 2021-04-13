import pandas as pd
import json
from davidyu_cfg import *
from functions.common.parseToDF import *

#return_data=get_uni_textfile(current_dir)

data_in_dir = "/home/davidyu/stock/data/history_data/dfcf_fuquan/raw_data_202012"
files = os.listdir(data_in_dir)
save_dir = "/home/davidyu/stock/data/history_data/dfcf_fuquan/stock_index"
for f1 in files:
    try:
        f = open(os.path.join(data_in_dir,f1))
        a1 = f.read()
        a2 = a1.split("\"")
        a3 = [x.split(",") for x in a2 if len(x)>3]
        df1 = pd.DataFrame(a3).dropna()
        df1.columns = ["dt","open","close","high","low","volume","money","x1","x2","x3","turnover_rate"]
        df1["stock_date"] = df1["dt"]
        df1["stock_index"] = f1[0:6]
        df2 = df1[df1["dt"]!="dt"].drop_duplicates()
        df2.to_csv(os.path.join(save_dir,f1.replace("txt","csv")),index=0)
    except Exception as e:
        pass
        logging.error(e)
        logging.info(f1)
