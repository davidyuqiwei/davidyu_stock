import os
from functions.data_dir import create_dir_if_not_exist

def save_the_table(new_table,dir_dadan,now_date,now_date_time,tag='no'):
    save_dir = os.path.join(dir_dadan,now_date)
    create_dir_if_not_exist(save_dir)
    if tag == 'no':
        save_file = os.path.join(save_dir,now_date_time+".csv")
    else:
        save_file = os.path.join(save_dir,now_date_time+'_'+tag+".csv")
    new_table.to_csv(save_file,index=0)



'''
def save_the_table(new_table,dir_dadan,now_date,now_date_time):
    save_dir = os.path.join(dir_dadan,now_date)
    create_dir_if_not_exist(save_dir)
    save_file = os.path.join(save_dir,now_date_time+".csv")
    new_table.to_csv(save_file,index=0)

'''


