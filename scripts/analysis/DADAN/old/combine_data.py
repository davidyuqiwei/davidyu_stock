from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *

now_date,now_date_time = get_the_datetime()

dir_dadan = data_dict.get("DADAN_offline")
#data_dir = os.path.join(dir_dadan,now_date)
data_dir = os.path.join(dir_dadan,"2020_01_14")

os.system("find %s | xargs cat  * > all.csv" %data_dir)
#os.system("sed -e '/0,1,2/d'  %sall.csv  > %sa.log" %(data_dir,data_dir))


