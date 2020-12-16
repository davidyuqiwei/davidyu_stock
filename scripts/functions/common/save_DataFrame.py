import os
from functions.data_dir import create_dir_if_not_exist
from functions.get_datetime import *


def save_the_table(new_table,dir_dadan,now_date,now_date_time,tag='no'):
    save_dir = os.path.join(dir_dadan,now_date)
    create_dir_if_not_exist(save_dir)
    if tag == 'no':
        save_file = os.path.join(save_dir,now_date_time+".csv")
    else:
        save_file = os.path.join(save_dir,now_date_time+'_'+tag+".csv")
    new_table.to_csv(save_file,index=0)

def save_df_date(save_dir,file_name_in,df,now_date=None):
    if now_date is None:
        now_date,now_date_time = get_the_datetime()
    file_name = file_name_in +'_' + now_date+'.csv'
    save_file = os.path.join(save_dir,file_name)
    df.to_csv(save_file,index=0)





'''
def save_the_table(new_table,dir_dadan,now_date,now_date_time):
    save_dir = os.path.join(dir_dadan,now_date)
    create_dir_if_not_exist(save_dir)
    save_file = os.path.join(save_dir,now_date_time+".csv")
    new_table.to_csv(save_file,index=0)

'''


