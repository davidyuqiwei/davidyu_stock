from davidyu_cfg import *
from functions.data_dir import *
from functions.get_datetime import *

#data_dir = data_dict.get("bankuai")
data_dir = data_dict.get("tmp")

file_in = "all_bankuai.csv"
#file_in = "bankuai_2020_02_20.csv"

df1 = pd.read_csv(os.path.join(data_dir,file_in))

df2 = df1[df1['stock_date']=='2020-05-22']

df2['涨跌幅'] = df2['涨跌幅'].astype('float')


