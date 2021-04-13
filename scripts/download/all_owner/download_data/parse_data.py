from davidyu_cfg import *
from functions.common.parseToDF import *
from functions.get_datetime import *
from functions.common.dfProcess import dfProcess
from functions.data_dir import create_dir_if_not_exist
from functions.update.cleanData import cleanData

def parse_data_to_df(file_in):
    save_dir = data_dict.get("all_owner")
    df1 = json_to_df(file_in)
    df2 = df1.get("data_out")
    with open(file_in) as f: ss = f.read()
    df2.iloc[0,:] = [ss.split("COMPANYCODE")[1].split(",")[0].replace(":",'').replace('\"','')]+df2.iloc[0,2:19].tolist()+["0"]
    col_dict={"COMPANYCODE":"80116563","SSNAME":"","SHAREHDNAME":"四川久远投资控股集团有限公司","SHAREHDTYPE":"投资公司",
                    "SHARESTYPE":"A股","RANK":1.0,"SCODE":"002258","SNAME":"利尔化学",
                    "RDATE":"2020-12-31T00:00:00","SHAREHDNUM":143484136.0,"LTAG":2998818442.4,
                    "ZB":0.274904761073159,"NDATE":"2021-03-06T00:00:00","BZ":"不变","BDBL":0.0,
                    "SHAREHDCODE":"80122121","SHAREHDRATIO":27.3626,"BDSUM":0.0}
    #col_name = [x for x in col_dict.keys()]+["test"]
    col_name = [x for x in col_dict.keys()]
    if df2.shape[1]==18:
        df2.columns = col_name
    if df2.shape[1]==19:
        df2.columns = col_name + ["test"]
    del df2['test']
    del df2['SSNAME']
    df2 = df2.dropna()
    df2["report_date"] = [x[0:10] for x in df2["NDATE"] ]
    df2["end_date"] = [x[0:10] for x in df2["RDATE"]]
    #df2.to_csv("data_out.csv",index=0)
    #df3 = df2[df2.SHAREHDNAME.str.len()>3]
    #df2.to_csv("data_out.csv",index=0)
    #df3.to_csv("data_out2.csv",index=0,encoding="utf_8_sig")
    df3 = df2
    
    df4 = df3[["SHAREHDNAME","SHAREHDTYPE","RANK","SCODE","SNAME","SHAREHDNUM","ZB","LTAG","BZ","BDSUM","report_date","end_date"]]
    df4.columns = ["gudong_name","gudong_type","rank","stock_index","stock_name","end_chigu_num_wan","ratio","last_chigu_num_wan","change_type",
            "change_num","report_date","end_date"]
    df4 = cleanData.columnToFloat(df4,["end_chigu_num_wan","last_chigu_num_wan","ratio","change_num"])
    df4["end_chigu_num_wan"] = df4["end_chigu_num_wan"]/10000
    df4["last_chigu_num_wan"] = df4["last_chigu_num_wan"]/10000
    df4["ratio"] = df4["ratio"] *100
    df4.gudong_type[df4["gudong_name"]=="香港中央结算有限公司"] = "QFII"
    now_date,now_date_time = get_the_datetime()
    # save data
    save_name = "dfcf_all_owner_"+now_date+".csv"
    df4.round(3).to_csv(os.path.join(save_dir,save_name),index=0,encoding="utf_8_sig")
    save_dir = "/home/davidyu/stock/data/shiny_data/data"
    file_shiny = "all_owner.csv"
    df4.round(2).to_csv(os.path.join(save_dir,file_shiny),index=0,encoding="utf_8_sig")
if __name__ == "__main__":
    file_in="test.txt"
    parse_data_to_df(file_in)

