import pandas as pd
from davidyu_cfg import *
from functions.rolling_regression import *
from functions.day_history.rollReg import rollRegDayHis


data_file = "/home/davidyu/stock/data/SH_SZ_index/SH_index.csv"

df1 = pd.read_csv(data_file)
df1.columns = [x.split(".")[1] for x in df1.columns]
x = df1
window =5
sort_col = "stock_date"
reg_col = "close"
df_rollreg = rolling_regression(x,window,sort_col,reg_col)


save_dir = tmp_data_dict.get("SH_index")
df_rollreg.round(3).to_csv(os.path.join(save_dir,"sh_index_rollReg.csv"),index=0)



