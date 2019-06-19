# coding: utf-8

## this script combine all the csv files in the folder
from package_path_define.path_define import *
from package_downloaddata.download_data_v1 import save_dir1
import pandas as pd


def combine_csv_in_folder(folder):
    files=os.listdir(folder)
    data_file='.//'.join([folder,files[0]])
    df1=pd.read_csv(data_file)
    for i in range(1,len(files)):
        data_file='.//'.join([folder,files[i]])
        df2=pd.read_csv(data_file)
        df1=pd.concat([df1,df2])
    return df1




market="shanghai"
#market="shenzhen"
## the stock index list
stock_path1='\\'.join([main_path_data,dir_stock_index,market])
sto2=os.listdir(stock_path1)

## where the data located
dir1="fuquan"
data_in_path1='\\'.join([main_path_data,dir1,market])
if not os.path.exists(data_in_path1):
    os.makedirs(data_in_path1)

## where to move the data
move_dir1="fuquan_combine"
move_dir='\\'.join([main_path_data,move_dir1,market])
if not os.path.exists(move_dir):
    os.makedirs(move_dir)

len_cri=(2016-1991+1)*4
for stk in sto2:
    sym=stk[:6]
    folder='\\'.join([data_in_path1,sym])  ## in each folder
    files=os.listdir(folder)
    len_file=len(files)
    if len_file==len_cri:
        df1=combine_csv_in_folder(folder)
        file_name1='_'.join([sym,'fuquan_all'])
        file_name=file_name1+'.csv'
        df1.to_csv(file_name,index=False)
        cmd1='mv %s %s'%(file_name,move_dir)
        #print cmd1
        print(sym)
        os.system(cmd1)
    else:
        pass
print('finish')

