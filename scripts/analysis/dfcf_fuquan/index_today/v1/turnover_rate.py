from davidyu_cfg import *
#from functions.pyspark_functions import *
from functions.baostock.stock_return import *
from functions.common.loadModule.load_module_kdj import *
from functions.common.macd_kdj.get_kdj import *
import pickle
#from m_features import *
#data_dir = os.path.join(data_dict.get("dfcf_fuquan"),"parse_data")

def load_index_300():
    df_300 = pd.read_csv("/home/davidyu/stock/data/common/index_300_raw.txt",header=None)
    index_300 = [str(x[0]).zfill(6) for x in df_300.values.tolist()]
    return index_300

def load_today_dfcf_data():
    data_dir = os.path.join(tmp_data_dict.get("dfcf_fuquan"))
    df1 = pd.read_csv(os.path.join(data_dir,"dfcf_fuquan.csv"))
    df1 = df1[df1["dt"]!="dt"].drop_duplicates()
    return df1

index_300 = load_index_300()
df1 = load_today_dfcf_data()
df1["turnover_rate"] = pd.to_numeric(df1["turnover_rate"])

df2 = df1[df1["dt"]==df1["dt"].max()]

df2 = df2.rename(columns={'x2':'change_ratio'})
df2_s = df2.sort_values("turnover_rate",ascending=False)
df_t_all = df2_s[["dt","turnover_rate","change_ratio","stock_index"]]
df_t_all.to_csv("./data/turnover_rate_all.csv",index=0)

df3 = df2[df2["stock_index"].isin(index_300)]
df3_s = df3.sort_values("turnover_rate",ascending=False)
df4 = df3_s[["dt","turnover_rate","change_ratio","stock_index"]]
df4.to_csv("./data/turnover_rate_hs300.csv",index=0)
