from davidyu_cfg import *
import pandas as pd
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.run_combine_all_csv import *


dir_dadan = data_dict.get("DADAN")
df1 = combine_csv_in_folder(dir_dadan)
df1.to_csv(os.path.join(dir_dadan,"DADAN_all.csv"),index=0)

