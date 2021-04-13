import pandas as pd
import json
from davidyu_cfg import *
from functions.check_dataframe_to_hive import *
from functions.data_dir import *
from functions.get_datetime import *
from functions.DFCF_json_to_df import *
import sys
from functions.get_text_file import *



def save_the_table(new_table,dir_dadan,now_date,now_date_time):
    save_dir = os.path.join(dir_dadan,now_date)
    create_dir_if_not_exist(save_dir)
    save_file = os.path.join(save_dir,now_date_time+".csv")
    new_table.to_csv(save_file,index=0)


def text_to_df(data_in_dir,file_name):
    #current_dir = os.path.abspath(os.path.dirname(__file__))
    #current_dir = "./"
    #filename,file_name_raw = get_text(current_dir)
    #filename2 = filename.replace(".txt",".csv")
    filename = os.path.join(data_in_dir,file_name)
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
    return df1,file_name
if __name__=='__main__':
    col_dict = {"HDDATE":"2021-03-23T00:00:00","HKCODE":"1000000973","SCODE":"601398","SNAME":"工商银行","PARTICIPANTCODE":"C00019","PARTICIPANTNAME":"香港上海>汇丰银行有限公司","SHAREHOLDSUM":382585271.0,"SHARESRATE":0.14,"CLOSEPRICE":5.4,"ZDF":-0.369,"SHAREHOLDPRICE":2065960463.4,"SHAREHOLDPRICEONE":12892555.260000229,"SHAREHOLDPRICEFIVE":-62783289.399999857,"SHAREHOLDPRICETEN":18719109.060000181,"MARKET":"001","ShareHoldSumChg":3790454.0,"Zb":0.0014190205532498205,"Zzb":0.0010734527337561942}
    data_dir = os.path.join(data_dict.get("dfcf_hugutong"),"raw_data")
    save_dir = os.path.join(data_dict.get("dfcf_hugutong"),"parse_data")
    files = os.listdir(data_dir)
    for file_name in files:
        df1,filename = text_to_df(data_dir,file_name)
        with open(os.path.join(data_dir,file_name)) as f: ss = f.read()
        if df1.shape[1]>2:
            df1.iloc[0,:] = [ss.split("HDDATE")[1][3:13]]+df1.iloc[0,2:].tolist()+["0"]
            if df1.shape[1]==18:
                df1.columns = [x for x in col_dict.keys()]
            if df1.shape[1]==19:
                df1.columns = [x for x in col_dict.keys()] + ["test"]
                del df1["test"]
            #print(df1)
            filename_out=os.path.join(save_dir,file_name.replace(".txt",".csv"))
            df1.to_csv(filename_out,index=0)

    
    '''
    dir_dadan = data_dict.get("dadan_DFCF")
    now_date,now_date_time = get_the_datetime()
    new_table = text_to_df()
    new_table['date'] = now_date
    save_the_table(new_table,dir_dadan,now_date,now_date_time)

    '''



"""
current_dir = os.path.abspath(os.path.dirname(__file__))
text_file,file_name_raw = get_text(current_dir)
columns = ["id","stock_index","stock_name","shijinglv"]
date_type = "day"
#save_dir = data_dict.get("shijinglv")
save_dir = "./"
df1 = json_to_df_raw(text_file,columns,date_type)
print(df1.shape)
now_date,_ = get_the_datetime()
df1.to_csv(os.path.join(save_dir,"shijinglv_"+now_date+".csv"),index=0)

"""

