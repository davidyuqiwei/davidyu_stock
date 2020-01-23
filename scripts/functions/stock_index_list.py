from davidyu_cfg import *
from functions.data_dir import data_dict

def get_stock_index_all_list():
    dir_basic_info = data_dict.get("basic_info")
    basic_file_name="stock_basic_info.csv"
    basic_file_in=os.path.join(dir_basic_info,basic_file_name)
    #stk_index_df = pd.read_csv(basic_file_in,header=None)
    stk_index_df = pd.read_csv(basic_file_in)
    stk_index_list = stk_index_df['code'].tolist()
    stk_index_list = [str(x).zfill(6) for x in stk_index_list]
    return stk_index_list

stk_index_list = get_stock_index_all_list()



