import pandas as pd
import json
from davidyu_cfg import *
from functions.common.parseToDF import *
import sys
#return_data=get_uni_textfile(current_dir)

input_file = sys.argv[1]
f = open(input_file)
a1 = f.read()
b=eval(a1)
df1 = pd.DataFrame(b,index=[0]).T.reset_index() 
df1.columns = ["name","val"]
x1 = [ x.split(",") for x in df1.val.tolist() ]  
df2 = pd.DataFrame(x1) 
df2.columns = ["bankuai_index","bankuai_name","company_cnt","avg_price","increase_val","increase_ratio",
        "total_shou","total_amount","lingzhang_stock_index","zhangdiefu","price",
        "stock_increase_ratio","stock_name"]
#print(df2)
df2.round(3).to_csv(input_file.replace("txt","csv"),index=0)




'''
files = os.listdir(data_dict.get("dfcf_fuquan"))
save_dir = os.path.join(data_dict.get("dfcf_fuquan"),"parse_data")
for f1 in files[0:10]:
    f = open(os.path.join(data_dict.get("dfcf_fuquan"),f1))
    a1 = f.read()
    a2 = a1.split("\"")                                                                                                                                                     
    a3 = [x.split(",") for x in a2 if len(x)>3]
    df1 = pd.DataFrame(a3)
    df1.to_csv(os.path.join(save_dir,f1.replace("txt","csv")),index=0)
'''
