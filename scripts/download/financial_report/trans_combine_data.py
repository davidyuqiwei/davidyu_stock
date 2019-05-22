import sys
import os
sys.path.append("../..")
from dir_control.data_dir import dir_basic_info,dir_financial_report,stk_index_list
import pandas as pd
files=os.listdir(dir_financial_report)
stk_in=set([ x.split("_")[0] for x in files ])

a1='002735'
file1=os.listdir(dir_financial_report)

fi='600856_2012.csv'
for i in stk_in:
    for fi in file1:
        if fi.split("_")[0] == i :
            df1=pd.read_csv(os.path.join(dir_financial_report,fi))



