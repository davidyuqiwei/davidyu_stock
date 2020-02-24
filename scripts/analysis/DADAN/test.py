from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist

basic_dir = data_dict.get("basic_info")

basic_df = pd.read_csv(os.path.join(basic_dir,"stock_basic_info.csv"))

basic_df1 =[str(x).zfill(6) for x in basic_df.code.tolist()]

basic_df['stock_index'] = basic_df['code']
df1 = pd.read_csv("2020_01_23.csv")
df2 = pd.merge(df1,basic_df,on="stock_index")
df2 = df2[['stock_index', 'stock_name', 'buy_num', 'sale_num', 'buy_sale_diff','industry']]

df2.to_excel("2020_01_23.xlsx",index=0)

