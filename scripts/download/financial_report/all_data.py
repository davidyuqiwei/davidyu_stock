import os
import sys
sys.path.append("../..")
from dir_control.data_dir_v1 import dir_financial_report
save_dir=dir_financial_report
print(dir_financial_report)
#os_str="cat %s/*.csv > all.csv"%(dir_financial_report)
os_str="find %s -name '*' | xargs -t -I {} cat {} >> all.csv "%(dir_financial_report)
os.system(os_str)



