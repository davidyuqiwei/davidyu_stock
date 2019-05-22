# coding: utf-8

import os
import pandas as pd
def combine_csv_in_folder(folder):
    files=os.listdir(folder)
    print(files)
    data_file='.//'.join([folder,files[0]])
    df1=pd.read_csv(data_file,encoding='ANSI')
    for i in range(1,len(files)):
    #for i in range(1,20):
        data_file='.//'.join([folder,files[i]])
        df2=pd.read_csv(data_file,encoding='ANSI')
        #df1.join(df2)
        df1=pd.concat([df1,df2.iloc[:,1:]], axis=1, join_axes=[df1.index])
    return df1
df1=combine_csv_in_folder("G:\\stock\\data\\financial_report\\shenzhen_test\\000002")
print(df1.head())
df1.to_csv("G:\\stock\\data\\financial_report\\shenzhen_test\\000002\\combine_data.csv",encoding='utf_8_sig')
