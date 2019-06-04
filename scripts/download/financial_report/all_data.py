import os
import sys
from davidyu_cfg import *
#sys.path.append("../..")
from dir_control.data_dir_v1 import dir_financial_report
save_dir = dir_financial_report

'''
print(dir_financial_report)
#os_str="cat %s/*.csv > all.csv" %(dir_financial_report)
os_str="find %s -name '*' | xargs -t -I {} cat {} >> all.csv "%(dir_financial_report)
os.system(os_str)
'''
import pandas as pd
for inputfile in os.listdir(save_dir):
    df1=pd.read_csv(os.path.join(save_dir,inputfile), header=None)
    df1.to_csv("all.csv", mode='a', index=False, header=False)

