from davidyu_cfg import *
from functions.common.loadModule.load_module_kdj import *


stock_index = '601398'
data_dir = os.path.join(data_path,"history_data","baostock","2020-12-17")

input_file = os.path.join(data_dir,stock_index+".csv")

out_file = "stock_index_kdj.csv"
df1 = pd.read_csv(os.path.join(data_dir,"stock_index_daily_data.csv"))
df1 = cleanData.cleanColName(df1)


def kdj_x(x):
    stock = DF_to_StockDataFrame(x)
    ss,tt = stock_kdj(stock)
    #print(ss)
    return ss,tt


group = df1
group = group.sort_values("dt")
df2,feature_name = kdj_x(group)
df_list.append(df2)
df_all = pd.concat(df_list)
df_all['dt'] = df_all["date"]
print(df_all)
df_all.round(2).to_csv(os.path.join(data_dir,out_file),index=0)
np.save(os.path.join(data_dir,"kdj_feature_name"),feature_name)





