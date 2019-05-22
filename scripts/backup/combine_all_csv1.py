## this script combine all the csv files in the folder
from package_path_define.path_define import *
from package_downloaddata.download_data_v1 import save_dir1
import pandas as pd


def combine_csv_in_folder(folder):
    files=os.listdir(folder)
    #df1=pd.DataFrame(columns=['date','open','high','close','low','volume','trade_amount','fuquan_factor','stockid'])
    df1=pd.DataFrame(columns=['Amount','Date','Onwer','Ratio','stockid'])
    for i in range(0,len(files)):
        data_file='.//'.join([folder,files[i]])
        with open("log.txt", "a") as text_file:
            text_file.write("run "+data_file+'\n')
        if os.path.getsize(data_file)> 100:
            try:
                df2=pd.read_csv(data_file)
                df1=pd.concat([df1,df2])
            except Exception as e:
                print(e)
                print(files[i])
    df1.to_csv(os.path.join(folder,'combine_data.csv'),index=False)
    return df1

#combine_csv_in_folder(data_for_sql)
