from davidyu_cfg import *
from functions.connect_url import url_opener
from functions.ForDownload import generate_stock_index,stk_index_list_gen
from functions.data_dir import *

data_dir = data_dict.get("tmp")

df1 = pd.read_csv(os.path.join(data_dir,"fushi_all.txt"),header=None)

df1.columns = ["index",'stock_date']

