from davidyu_cfg import *
from functions.data_dir import *
from functions.colNames import setColname

data_dir = tmp_data_dict.get("bankuai")
data_file = os.path.join(data_dir,"bankuai.csv")

df1 = pd.read_csv(data_file)
df1.columns = setColname().bankuai()

df1.to_csv(data_file,index=0,header=None)




