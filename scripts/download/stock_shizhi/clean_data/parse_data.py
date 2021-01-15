import pandas as pd
import json
from davidyu_cfg import *
from functions.common.parseToDF import *

data_in_dir = os.path.join(data_dict.get("stock_shizhi"),"raw_data")
files = os.listdir(data_in_dir)
save_dir = os.path.join(data_dict.get("stock_shizhi"),"parse_data")
for f1 in files:
    try:
        f = open(os.path.join(data_in_dir,f1))
        a1 = f.read()
        a2 = "{"+a1
        a2_dict = eval(a2)
        df1 =  pd.DataFrame(a2_dict,index=[0])
        df1["stock_date"] = df1["opendate"]
        df1["dt"] = df1["opendate"]
        df1["stock_index"] = f1[0:6]
        df1.to_csv(os.path.join(save_dir,f1),index=0)
    except Exception as e:
        pass
        logging.error(e)
        logging.info(f1)

