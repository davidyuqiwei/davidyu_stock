# coding: utf-8

## this script combine all the csv files in the folder
#from package_path_define.path_define import *
#from package_downloaddata.download_data_v1 import save_dir1
import pandas as pd
import os
from os import walk
def combine_csv_in_folder_raw(folder):
    files = os.listdir(folder)
    data_file = os.path.join(folder,files[0])
    df1 = pd.read_csv(data_file)
    for i in range(1,len(files)):
        data_file = os.path.join(folder,files[i])
        df2 = pd.read_csv(data_file)
        df1 = pd.concat([df1,df2])
    return df1

def combine_csv_in_folder(folder):
    '''
    combine all the csv file in the sub-folder
    '''
    csv_list = []
    for dirname,dirs,files in walk(folder):
        for filename in files:
            if 'csv' in filename:
                filename = os.path.join(dirname,filename)
                csv_list.append(filename)
            else:
                pass
    print("total csv files:"+  str(len(csv_list)))
    df1 = pd.read_csv(csv_list[0])
    #print(df1)
    for i in range(1,len(csv_list)):
        #data_file = pd.read_csv(csv_list[i])
        #print(i)
        df2 = pd.read_csv(csv_list[i])
        df1 = pd.concat([df1,df2])
    return df1

def list_all_files_in_folder(folder):
    '''
    combine all the csv file in the sub-folder
    '''
    csv_list = []
    for dirname,dirs,files in walk(folder):
        for filename in files:
            filename = os.path.join(dirname,filename)
            csv_list.append(filename)
    return csv_list



'''
    files = os.listdir(folder)
    data_file = os.path.join(folder,files[0])
    df1 = pd.read_csv(data_file)
    for i in range(1,len(files)):
        data_file = os.path.join(folder,files[i])
        df2 = pd.read_csv(data_file)
        df1 = pd.concat([df1,df2])

'''


