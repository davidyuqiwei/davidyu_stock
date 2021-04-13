from davidyu_cfg import *
from functions.common.parseToDF import *
from functions.get_datetime import *
from functions.common.dfProcess import dfProcess
from functions.data_dir import create_dir_if_not_exist
#file_in = "/home/davidyu/stock/data/dfcf_hexinticai/601398_hexinticai.txt"
data_dir = data_dict.get("dfcf_hexinticai")
files_dir = os.path.join(data_dir,"raw_data")
save_dir = os.path.join(data_dir,"parse_data")

files = os.listdir(files_dir)

for f1 in files:
    file_in = os.path.join(files_dir,f1)
    df1 = json_to_df(file_in)
    df2 = df1.get("data_out")
    stock_index = df2.iloc[0,1][0:6]
    ticai = df2.iloc[0,6]
    ticai1 = pd.DataFrame(ticai.split(" "))
    ticai1["stock_index"] = stock_index
    ticai1.columns = ["ticai","stock_index"]
    save_file = f1.replace("txt","csv")
    save_file1 = os.path.join(save_dir,save_file)
    ticai1.to_csv(save_file1,index=0)
