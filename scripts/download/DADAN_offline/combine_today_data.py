from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *

'''
combine today DADAN data
@time:   2020-02-03
'''



if __name__ =='__main__':
    now_date,now_date_time = get_the_datetime()  ## the now_date is like "2019_11_08"
    #now_date = "2020_01_30"
    dir_dadan = data_dict.get("DADAN_offline")
    data_dir = os.path.join(dir_dadan,now_date)
    print(data_dir)
    df1 = combine_csv_in_folder_raw(data_dir)
    df1.columns = ["stock_index","stock_name", \
            "trade_time","price","trade_num","trade_shou", \
            "status","price_change_rate","price_change_ratio","look","stock_date"]
    df1['stock_index'] = [ str(x).zfill(6) for x in df1.stock_index.tolist()]
    df1['day'] = [x.replace("_","-") for x in df1.stock_date.tolist()]
    tmp_dir = data_dict.get("tmp")
    save_data_name = "DADAN_offline_"+now_date+".csv"
    df1.to_csv(os.path.join(tmp_dir,save_data_name),index=0)



