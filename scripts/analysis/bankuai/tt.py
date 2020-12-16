from davidyu_cfg import *
from functions.data_dir import *
from functions.get_datetime import *
from functions.run_combine_all_csv import *

#data_dir = data_dict.get("history_data")
data_dir1 = os.path.join(data_path,"history_data","bankuai")
df1 = combine_csv_in_folder(data_dir1)

#file_in = "all_bankuai.csv"
#file_in = "bankuai_2020_02_20.csv"

#df1 = pd.read_csv(os.path.join(data_dir,file_in))

df2 = df1[df1['stock_date']>='2020-09-01']

df2['涨跌幅'] = df2['涨跌幅'].astype('float')
df2 = df2.sort_values("涨跌幅",ascending=False)
df3 = df2[['板块',"涨跌幅","领涨股","当前价","涨跌幅.1","stock_date"]]
df3.sort_values("涨跌幅")
df3.sort_values("涨跌幅.1")

df3.to_excel("bankuai_test.xlsx",index=0)


df3[df3["板块"] == "水产品"].sort_values("stock_date")
df3[df3["板块"] == "生物疫苗"].sort_values("stock_date")


#df1 = pd.read_csv("/home/davidyu/stock/data/tmp_data/bankuai/bankuai.csv")



