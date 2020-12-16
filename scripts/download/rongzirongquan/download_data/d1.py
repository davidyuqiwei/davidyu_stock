import pandas as pd
import json
from davidyu_cfg import *
from functions.check_dataframe_to_hive import *
from functions.data_dir import *
from functions.get_datetime import *
from functions.DFCF_json_to_df import *
import sys
from functions.get_text_file import *
from functions.colNames import *

def text_to_df():
    #current_dir = os.path.abspath(os.path.dirname(__file__))
    save_dir = data_dict.get("rongzirongquan")
    current_dir = "./"
    filename,file_name_raw = get_text(current_dir)

    f = open(filename)
    a1 = f.read()

    s1 = a1.split("}")
    strings = []
    for i in s1:
        try:
            i1 = i[2:]
            s2 = i1.split(",")
            s3 = [x.split(":")[1] for x in s2]
            s3 = [x.replace("\"","") for x in s3]
            #for j in [2,3,4,7,13]:
                #s3[j] = s3[j].encode("latin1").decode("gb2312")
            strings.append(s3)
        except:
            pass
    df1 = pd.DataFrame(strings)
    out_name = os.path.join(save_dir,filename.replace("txt","csv"))
    df1.to_csv(out_name,index=0)
    return df1
df1 = text_to_df()
#print(df1)
