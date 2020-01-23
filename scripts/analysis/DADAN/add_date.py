from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *

dir_dadan = data_dict.get("DADAN")

all_csv = list_all_files_in_folder(dir_dadan)

j = 0
for k in all_csv:
    a2 = k
    [dirname,filename] = os.path.split(a2)
    date_raw = filename[0:10]
    df1 = pd.read_csv(k)
    #print(k)
    if 'date' in df1.columns:
        pass
    else:
        df1['date'] = date_raw
    #print(df1.head())
    df1.to_csv(k,index=0)

