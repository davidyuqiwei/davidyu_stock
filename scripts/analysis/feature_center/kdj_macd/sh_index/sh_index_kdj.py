from davidyu_cfg import *
from functions.common.loadModule.load_module_kdj import *

data_dir = data_dict.get("test")
out_file = "sh_index_kdj.csv"
df1 = pd.read_csv(os.path.join(data_dir,"sh_index.csv"))
df1 = cleanData.cleanColName(df1)


stock = DF_to_StockDataFrame(df1)
df_stock,feature_name = stock_kdj(stock)
df_stock["dt"] = df_stock["stock_date"] 
df_stock.round(2).to_csv(os.path.join(data_dir,out_file),index=0)
np.save(os.path.join(data_dir,"kdj_feature_name"),feature_name)





