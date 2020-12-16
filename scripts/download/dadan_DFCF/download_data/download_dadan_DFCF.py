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



def save_the_table(new_table,dir_dadan,now_date,file_name):
    #save_dir = os.path.join(dir_dadan,now_date)
    save_dir = dir_dadan
    create_dir_if_not_exist(save_dir)
    save_file = os.path.join(save_dir,file_name)
    new_table.columns = setColname().dadan_DFCF()
    new_table.to_csv(save_file,index=0)


def text_to_df():
    #current_dir = os.path.abspath(os.path.dirname(__file__))
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
    return df1
if __name__=='__main__':
    from functions.update.cleanData import cleanData
    
    #dir_dadan = data_dict.get("dadan_DFCF")
    dir_dadan = "./"
    now_date,now_date_time = get_the_datetime()
    new_table = text_to_df()
    new_table['date'] = now_date
    new_table = cleanData.columnToFloat(new_table,["new_price","today_increase_ratio","zhuli_liuru",
            'chaodadan_liuru', 'chaodadan_liuru_ratio','dadan_liuru', 'dadan_liuru_ratio', 'zhongdan_liuru',
                'zhongdan_liuru_ratio', 'xiaodan_liuru', 'xiaodan_liuru_ratio','zhuli_liuru_ratio'])
    file_name = sys.argv[1]
    save_the_table(new_table,dir_dadan,now_date,file_name)



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
