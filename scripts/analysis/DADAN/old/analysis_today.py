from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *

'''
update the date in df 
raw dataframe has not cover the download date,
which cannot choose by date
@ update time 2019-11-25
'''



def status_sum(df2,status):
    df3 = df2[df2["status"] == status] #get the data is in status
    df4 = df3.groupby(["stock_index","stock_name"])["trade_num"].sum().reset_index() # sum the trade number of the status
    if status == "买盘":
        df4.columns = ["stock_index","stock_name","buy_num"]
    elif status == "卖盘":
        df4.columns = ["stock_index","stock_name","sale_num"]
    return df4
def DADAN_diff_stat(df_input):
    df2 = df_input.drop_duplicates()
    df4 = status_sum(df2,"买盘")
    df6 = status_sum(df2,"卖盘")
    ## 
    df_merge = pd.merge(df4,df6,how='left',on = ["stock_index","stock_name"])
    df_merge = df_merge.fillna(0)
    df_merge["buy_sale_diff"] = df_merge["buy_num"]-df_merge["sale_num"]
    df_merge1 = df_merge.sort_values("buy_sale_diff",ascending=False)
    #print(df_merge1)
    return df_merge1

if __name__ =='__main__':
    now_date,now_date_time = get_the_datetime()  ## the now_date is like "2019_11_08"
    #now_date = "2020_01_23"
    dir_dadan = data_dict.get("DADAN")
    data_dir = os.path.join(dir_dadan,now_date)
    print(data_dir)
    df1 = combine_csv_in_folder(data_dir)
    df1.columns = ["stock_index","stock_name", \
            "trade_time","price","trade_num","trade_shou", \
            "status","price_change_rate","price_change_ratio","look","date"]
    #df1.to_csv("DADAN_sample.csv",index=0)
    df_merge1 = DADAN_diff_stat(df1)
    print(df_merge1.head(50))
    #df_merge1.to_csv("2020_01_23.csv",index=0,encoding="utf_8_sig")
    print(df_merge1.tail(30))
    df_merge2 = df_merge1[df_merge1.sale_num.isna()]   
    df_merge3 = df_merge2.sort_values("buy_num",ascending=False)  
    


