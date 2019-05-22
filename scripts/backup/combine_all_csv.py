# coding: utf-8

## this script combine all the csv files in the folder
from package_path_define.path_define import *
from package_downloaddata.download_data_v1 import save_dir1
import pandas as pd
from package_functions.combine_allCsv_inFolder import combine_csv_in_folder


path_stock_owner_liutong=r'\\'.join([main_path,"data_to_sql_owner"])
#os.system('ls')
#df1=combine_csv_in_folder(path_stock_owner_liutong)
#print(df1.head())
'''
file_name1="data_combine.csv"
file_name=r'\\'.join([path_stock_owner_liutong,file_name1])
file_name2="data_combine_tr.csv"
file_name_tr=r'\\'.join([path_stock_owner_liutong,file_name2])
os.system('iconv -f utf_8_sig -t utf-8 '+file_name +' >'+file_name_tr)
'''
df1=pd.read_csv(path_stock_owner_liutong+'\\data_combine.csv')
df1=df1.round(2).iloc[1:30,]
df1.to_csv(path_stock_owner_liutong+'\\data_combine.csv_tr.csv',encoding="utf-8",index=False)

#def combine_csv_in_folder(folder,save_name="data_combine.csv"):
#    files=os.listdir(folder)
#    data_file='.//'.join([folder,files[0]])
#    df1=pd.read_csv(data_file)
#    for i in range(1,len(files)):
#    #for i in range(1,20):
#        data_file='.//'.join([folder,files[i]])
#        df2=pd.read_csv(data_file)
#        df1=pd.concat([df1,df2])
#    df1.to_csv('.//'.join([folder,save_name]),index=False)
#    return df1
#
#path_stock_owner_liutong=r'\\'.join([main_path,"data_to_sql_owner"])
#df1=combine_csv_in_folder(path_stock_owner_liutong)


# In[16]:


## this script combine all the csv files in the folder
#import pandas as pd
#import os

# In[7]:


#print df1.head()
#file_name1="stock_owner_liutong_combine.csv"
