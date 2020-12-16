import pandas as pd
from davidyu_cfg import *
from functions.data_dir import *
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import *
import baostock as bs

year = sys.argv[1]
out_file = "bao_test_"+str(year)+".csv"
data_dir = data_dict.get("baostock")
files = os.listdir(data_dir)
print(files)
for f1 in files:
    try:
        df1 = pd.read_csv(os.path.join(data_dir,f1))
        df2 = df1
        df2["year"] = df1["date"]
        df2["year"] = [x[0:4] for x in df1["date"].values]  
        df2["code"] = [x[3:] for x in df1["code"].values]  
        df3 = df2[df2["year"]==str(year)]
        df3.to_csv(out_file,index=0,header=None,mode='a')
    except:
        pass



