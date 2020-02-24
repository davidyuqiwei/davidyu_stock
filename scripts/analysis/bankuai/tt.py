from davidyu_cfg import *
from functions.data_dir import *
from functions.get_datetime import *

data_dir = data_dict.get("bankuai")

file_in = "bankuai_2020_02_20.csv"

df1 = pd.read_csv(os.path.join(data_dir,file_in))

