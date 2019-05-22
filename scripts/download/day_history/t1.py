import tushare as ts
import sys
sys.path.append("..\..")
from dir_control.dir_setup import *
#from download.test.t1 import *
#import download.test.t1



save_dir=path_dict["day_history"]
file_name="test.csv"
save_file_name=dir_join_str.join([save_dir,file_name])
#print(save_dir)


start_date="2015-01-01"
end_date="2015-01-5"
#df = ts.get_tick_data('600848',date='2018-12-12',src='tt')
df=ts.get_h_data('002337', start=start_date, end=end_date)

df.to_csv(save_file_name)


#print(df.head(10))
#print("test")

