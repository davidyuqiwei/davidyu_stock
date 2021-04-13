from davidyu_cfg import *
from functions.common.parseToDF import *
import sys
import json
from functions.get_datetime import *

file1 = sys.argv[1]

f = open(file1)
a1 = f.read()
a2 = json.loads(a1)

aa = a2.get('zygd')
a3 = a2.get('lsgqbd')
#pd.DataFrame(aa)

df1_list = []

for x1 in aa:
    dt = x1.get("date")
    df_tmp = pd.DataFrame(x1.get("gd"))
    df_tmp["dt"] = dt
    df1_list.append(df_tmp)
df1 = pd.concat(df1_list)
df2 = pd.DataFrame(a3)

now_date,now_date_time = get_the_datetime()
stock_index = file1.split(".txt")[0]
df1.to_csv(stock_index+'_'+now_date+"_ownerlist.csv",index=0)
df2.to_csv(stock_index+'_'+now_date+"_ownerchange.csv",index=0)



