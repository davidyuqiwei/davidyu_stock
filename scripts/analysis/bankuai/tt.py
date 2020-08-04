from davidyu_cfg import *
from functions.data_dir import *
from functions.get_datetime import *
from functions.run_combine_all_csv import *

data_dir = data_dict.get("bankuai")
#data_dir = data_dict.get("tmp")
df1 = combine_csv_in_folder(data_dir)

#file_in = "all_bankuai.csv"
#file_in = "bankuai_2020_02_20.csv"

#df1 = pd.read_csv(os.path.join(data_dir,file_in))

df2 = df1[df1['stock_date']=='2020-07-06']

df2['涨跌幅'] = df2['涨跌幅'].astype('float')
df2 = df2.sort_values("涨跌幅",ascending=False)
df2[['板块',"涨跌幅","领涨股"]]
