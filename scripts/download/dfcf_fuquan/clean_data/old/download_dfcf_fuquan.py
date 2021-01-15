import pandas as pd
import json
from davidyu_cfg import *
from functions.common.parseToDF import *

#return_data=get_uni_textfile(current_dir)

files = os.listdir(data_dict.get("dfcf_fuquan"))
save_dir = os.path.join(data_dict.get("dfcf_fuquan"),"parse_data")
for f1 in files[0:10]:
    f = open(os.path.join(data_dict.get("dfcf_fuquan"),f1))
    a1 = f.read()
    a2 = a1.split("\"")                                                                                                                                                     
    a3 = [x.split(",") for x in a2 if len(x)>3]
    df1 = pd.DataFrame(a3)
    df1.to_csv(os.path.join(save_dir,f1.replace("txt","csv")),index=0)

