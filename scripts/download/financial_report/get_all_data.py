import os
import sys
sys.path.append("../..")
from dir_control.data_dir_v1 import data_dict,stk_index_list

dir_day_history_insert=data_dict.get("financial_report")
os_str="cat %s/*.csv > all.csv"%(dir_day_history_insert)

print(os_str)
os.system(os_str)


