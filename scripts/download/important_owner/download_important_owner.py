import pandas as pd
import json
from davidyu_cfg import *
from functions.check_dataframe_to_hive import *
from functions.data_dir import *
from functions.get_datetime import *
from functions.DFCF_json_to_df import *
import sys
from functions.get_text_file import *

current_dir = os.path.abspath(os.path.dirname(__file__))



filename,file_name_raw = get_text(current_dir)

f = open(filename,encoding="latin1")
a1 = f.read()
#a2 = a1.replace("'", "\"")
#raw_json = json.loads(a1)

#s1 = a1.split("}")[0][2:]
#s2 = s1.split(",")

#q1 = a1.split("}")[1]

s1 = a1.split("}")
strings = []
for i in s1:
    try:
        i1 = i[2:]
        s2 = i1.split(",")
        s3 = [x.split(":")[1] for x in s2]
        s3 = [x.replace("\"","") for x in s3]
        for j in [2,3,4,7,13]:
            s3[j] = s3[j].encode("latin1").decode("gb2312")
        strings.append(s3)
    except:
        pass

df1 = pd.DataFrame(strings)
input_in = sys.argv[1]
name = input_in
save_dir = data_dict.get("important_owner")
now_date,_ = get_the_datetime()
df1.to_csv(os.path.join(save_dir,name+"_"+now_date+".csv"),index=0)

'''
columns = ["id","stock_index","stock_name","shijinglv"]
date_type = "day"
#save_dir = data_dict.get("shijinglv")
save_dir = "./"
df1 = json_to_df_raw(text_file,columns,date_type)
print(df1.shape)
now_date,_ = get_the_datetime()
df1.to_csv(os.path.join(save_dir,"shijinglv_"+now_date+".csv"),index=0)

'''

