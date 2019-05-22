import os
import pandas as pd
def combine_csv_in_folder(folder,save_name="data_combine.csv"):
    files=os.listdir(folder)
    data_file='.//'.join([folder,files[0]])
    df_pro='.//'.join([folder,"data_combine.csv"])
    os.system("rm -rf "+df_pro)
    df1=pd.read_csv(data_file,encoding='utf_8_sig')
    for i in range(1,len(files)):
    #for i in range(1,20):
        data_file='.//'.join([folder,files[i]])
        print(files[i])
        df2=pd.read_csv(data_file,encoding='utf_8_sig')
        df1=pd.concat([df1,df2])
    df1.to_csv('.//'.join([folder,save_name]),index=False,header=False,encoding='utf_8_sig')
    return df1


