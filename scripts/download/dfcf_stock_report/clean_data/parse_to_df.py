from davidyu_cfg import *
from functions.common.parseToDF import *
from functions.get_datetime import *

now_date,now_date_time = get_the_datetime()
file_in = sys.argv[1]
save_dir = os.path.join(data_dict.get("dfcf_bankuai_zijin"),"parse_data")
df1 = json_to_df("test.txt")
df2 = df1.get("data_out")
#df2.columns = ["bankuai_index","test","bankuai_name_ch","zijin_liuru"]
df2["dt"] = now_date
#print(df1.get("data_out"))
print(df2)

df3 = df2.iloc[:,[0,1,2,4,5,6,23,45]]

save_file = os.path.join(save_dir,file_in.replace(".txt",".csv"))
#df2.to_csv(save_file,index=None)

