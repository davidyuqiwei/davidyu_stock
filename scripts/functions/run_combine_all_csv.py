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



