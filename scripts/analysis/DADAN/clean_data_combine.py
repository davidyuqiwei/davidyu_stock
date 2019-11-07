from davidyu_cfg import *
from functions.run_combine_all_csv import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
import datetime

def print_calc_time(func):
    def wrapper(*args, **kw):  
        start_time = datetime.datetime.now() 
        func(*args, **kw) 
        end_time = datetime.datetime.now()
        ss = end_time - start_time
        print('Function <{}> run time is {}s.'.format(func.__name__, ss))
    return wrapper

@print_calc_time
def combine_clean_data():
    dir_dadan = data_dict.get("DADAN")
    folder = dir_dadan
    df_all = pd.DataFrame(columns=('0','1','2','3','4','5','6','7','8','9','date'))
    for dirname,dirs,files in walk(folder):
        try:
            date_sig = dirname.split("/")[-1:][0]
            date_in = datetime.datetime.strptime(date_sig,"%Y_%m_%d").strftime("%Y-%m-%d")
            print(dirname)
            df1 = combine_csv_in_folder_raw(dirname)
            df1['date'] = date_in
            df_all = pd.concat([df_all,df1])  
        except:
            pass
    df_out = df_all.drop_duplicates()
    df_out.to_csv("test.csv",index=0)
    return df_out
df_out = combine_clean_data()
#print(df_all.shape)
#data_dir = os.path.join(dir_dadan,now_date)


