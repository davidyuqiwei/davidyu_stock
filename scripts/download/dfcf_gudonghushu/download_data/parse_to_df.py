from davidyu_cfg import *
from functions.common.parseToDF import *
from functions.get_datetime import *
from functions.common.dfProcess import dfProcess
from functions.data_dir import create_dir_if_not_exist
#now_date,now_date_time = get_the_datetime()
#file_in = "dfcf_bankuai_2021-01-18.txt"

def to_df(file_in):
    try:
        save_dir = os.path.join(data_dict.get("dfcf_gudonghushu"),"parse_data")
        create_dir_if_not_exist(save_dir)
        df1 = json_to_df(file_in)
        df2 = df1.get("data_out")
        with open(file_in) as f: ss = f.read()
        df2.iloc[0,:] = [ss.split("HolderNum")[1].split(",")[0].replace(":",'').replace('\"','')]+df2.iloc[0,2:15].tolist()+["0"]
        df2.columns = ["HolderNum","PreviousHolderNum","HolderNumChange"
,"HolderNumChangeRate","RangeChangeRate",
"EndDate","HolderAvgCapitalisation","HolderAvgStockQuantity",
"TotalCapitalisation","CapitalStock","NoticeDate",
"CapitalStockChange","CapitalStockChangeEvent",
"ClosePrice","test"]
        del df2['test']
        df2["dt"] = df2["EndDate"]
        df2['stock_index'] = file_in[0:6]
        df3 = dfProcess.col2Float(df2,["HolderNum","PreviousHolderNum","HolderNumChange"])
        save_file = os.path.join(save_dir,file_in.replace(".txt",".csv"))
        #save_file = "./test.csv"
        df2.to_csv(save_file,index=None)
    except:
        save_dir = os.path.join(data_dict.get("dfcf_gudonghushu"),"parse_data")
        #save_dir="./"
        save_file = os.path.join(save_dir,file_in.replace(".txt",".csv"))
        df2=pd.DataFrame()
        df2.to_csv(save_file,index=None)
if __name__ == '__main__':
    file_in = sys.argv[1]
    to_df(file_in)
