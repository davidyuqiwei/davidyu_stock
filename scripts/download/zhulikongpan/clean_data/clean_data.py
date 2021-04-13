import pandas as pd
from davidyu_cfg import *
from functions.common.listProcess import *
from functions.common.dfProcess import *
from functions.common.loadModule.load_module_kdj import *

df1 = pd.read_csv("/home/davidyu/stock/data/tmp/zhulikongpan.csv",header=None)

df2 = df1.iloc[:,[0,1,2,8,9]]
df2.columns =['dt',"stock_index","stock_name","kongpan_ratio","kongpan_nm"]

df2["dt"] = [x[0:10] for x in df2["dt"].values.tolist()]
save_dir = tmp_data_dict.get("zhulikongpan")


stock_list = df2["stock_index"].unique().tolist()
for s1 in stock_list:
    df3 = df2[df2["stock_index"]==s1]
    df3.drop_duplicates().round(2).to_csv(os.path.join(save_dir,str(s1).zfill(6)+".csv"),index=0)


#column_names = ["stock_date","stock_index","stock_name","price","kongpan_ratio","kongpan_cn"]

#df.columns = column_names
#df1.sort_values("kongpan_ratio",ascending=False).head(30)

#df1.to_csv("zhulikongpan_test.csv",index=0)














