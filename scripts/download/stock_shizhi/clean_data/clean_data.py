import pandas as pd
import json
from davidyu_cfg import *
from functions.common.parseToDF import *
from functions.common.TimeMake import *
from functions.common.dfProcess import *

now_date,now_date_time = timeFunc.get_the_datetime()
file_in = "stock_shizhi.csv"
#file_name = "stock_shizhi_"+now_date+".csv"
data_dir = tmp_data_dict.get("stock_shizhi")
input_file = os.path.join(data_dir,file_in)
df1 = pd.read_csv(input_file)
df1 = df1[df1["dt"]!="dt"]
df2 = df1[["curr_capital","trade","dt","stock_index"]]
df2 = dfProcess.col2Float(df2,["curr_capital","trade"])
df3 = df2.copy()
df3["liutong_capital"] = df2["curr_capital"]*df2["trade"]/10000

df3.round(2).to_csv(input_file,index=0)
