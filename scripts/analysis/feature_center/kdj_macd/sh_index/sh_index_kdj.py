from davidyu_cfg import *
from functions.common.loadModule.load_module_kdj import *
from functions.common.macd_kdj.get_kdj import *


data_dir = data_dict.get("test")
out_file = "sh_index_kdj.csv"
df1 = pd.read_csv(os.path.join(data_dir,"sh_index.csv"))
df = cleanData.cleanColName(df1)

df3 = df.groupby("stock_index").apply(lambda x: kdj_x(x)).reset_index(drop=True)
df3 = df3.groupby("stock_index").apply(lambda x: new_kdj(x,16,3,3)).reset_index(drop=True)
df3 = df3.groupby("stock_index").apply(lambda x: new_macd(x,'close',5,35,5)).reset_index(drop=True)



def get_roll_mean(df3,cols,window):
    for i in cols:
        new_name = "roll_mean_"+i+"_"+str(window)
        df3[new_name] = df3[i].rolling(window=window).mean()
    return df3
df4 = get_roll_mean(df3,["close","open","high","low"],5)

df4.to_csv("pred1.csv",index=0)

#stock = DF_to_StockDataFrame(df1)
#df_stock,feature_name = stock_kdj(stock)
#df_stock["dt"] = df_stock["stock_date"] 
#df_stock.round(2).to_csv(os.path.join(data_dir,out_file),index=0)
#np.save(os.path.join(data_dir,"kdj_feature_name"),feature_name)





