from davidyu_cfg import *
from functions.common.parseToDF import *
from functions.get_datetime import *

now_date,now_date_time = get_the_datetime()
file_in = sys.argv[1]
#file_in = "dfcf_bankuai_2021-01-18.txt"
save_dir = os.path.join(data_dict.get("dfcf_bankuai"),"parse_data")
df1 = json_to_df(file_in)
df2 = df1.get("data_out")
#df2.columns = ["bankuai_index","test","bankuai_name_ch","zijin_liuru"]
df2["dt"] = now_date
#rint(df2)
#print(df1.get("data_out"))

save_file = os.path.join(save_dir,file_in.replace(".txt",".csv"))
df2.to_csv(save_file,index=None)

