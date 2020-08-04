import pandas as pd
from davidyu_cfg import *
from functions.stockstats.stockStats import *
from functions.rolling_regression import *
from functions.stock_feature.mergeData import mergeData
# remove first two lines

raw_data_dir = tmp_data_dict.get("qianlong_day_history")
data_dir = os.path.join(raw_data_dir,"test")
files = os.listdir(data_dir)

#file_in = "/home/davidyu/stock/data/tmp_data/qianlong_day_history/test/000089.txt"

frames = []
for f in files:
    file_in = os.path.join(data_dir,f)
    df1 = pd.read_csv(file_in,error_bad_lines=False,encoding="latin1",sep="\t")
    df1.columns = ["stock_date","open","high","low","close","volume","money", 
        "KLINE.5MA","KLINE.10MA1","KLINE.30MA3","KLINE.200MA6","KLINE.300MA7" 
        ,"kdj_k","kdj_d","kdj_j","macd_dif","macd","macd_dif_macd","stock_index"]
    df1["stock_index"] = f[0:6]
    frames.append(df1)

df_all = pd.concat(frames)

def data_process(df2,columns_list):
    for col in columns_list:
        df2[col] = [x.replace("    ","") for x in df2[col].tolist()]
        df2 = df2.replace("----",np.nan)
    return df2
columns_list = ["kdj_j","kdj_k","kdj_d","macd_dif","macd","macd_dif_macd"]
df3 = data_process(df_all,columns_list).dropna()

window = 5
df_roll_reg = df3.groupby("stock_index").apply(lambda x: rolling_regression(x,window,"stock_date","close"))

df2 = df_roll_reg.reset_index(drop=True) 
df2 = df2[df2["slope_num_in"] ==5]
df2["slopes"] = mergeData.regPN(df2,'slopes')["slopes"]
df3 = df2[["kdj_k","kdj_d","kdj_j","macd_dif","macd","macd_dif_macd","slopes"]]

tmp_path = raw_data_dir
save_file = "test.csv"
save_file_name = os.path.join(tmp_data_path,save_file)
df3.to_csv(save_file_name,index=0)




df2 = df1.replace("    ----",-999)
df2 = df1.replace("    ","")
df3 = df2[df2["kdj_j"]>-900]

df2["kdj_j"] = [x.replace("    ","") for x in df2["kdj_j"].tolist()] 
df2 = df2.replace("----",-999)
df2["kdj_j"] = df2["kdj_j"].astype(float)
df3 = df2[df2["kdj_j"]>-900]

df1["close"] = df1["close"].astype(float)
#df2["kdj_j"] = df2["kdj_j"].astype(float)

df1["kdj_j"] = df1["kdj_j"].astype(float)
df_roll_reg = rolling_regression(df2,window,"stock_date","close")
df_roll_reg[df_roll_reg["kdj_j"]<0]






