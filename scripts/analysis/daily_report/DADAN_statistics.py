from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.colNames import *
from functions.daily_report import dailyReport
from functions.DF_process import changeStockIndex
'''
update the date in df 
raw dataframe has not cover the download date,
which cannot choose by date
@ update time 2019-11-25

@ update colNames
'''

def status_sum(df2,status):
    df3 = df2[df2["status"] == status]
    df4 = df3.groupby(["stock_index","stock_name"])["trade_num","trade_shou"].sum().reset_index() ## trade money and shou sum
    if status == "买盘":
        df4.columns = ["stock_index","stock_name","buy_num","buy_shou"]
    elif status == "卖盘":
        df4.columns = ["stock_index","stock_name","sale_num","sale_shou"]
    return df4
def DADAN_diff_stat(df_input):
    df2 = df_input.drop_duplicates()
    df_buy = status_sum(df2,"买盘")
    df_sell = status_sum(df2,"卖盘")
    ## 
    df_merge = pd.merge(df_buy,df_sell,how='left',on = ["stock_index","stock_name"]) # merge join, on 'stock_index' and 'stock_name'
    df_merge = df_merge.fillna(0)
    df_merge["buy_sale_diff"] = df_merge["buy_num"]-df_merge["sale_num"]
    df_merge["buy_sale_diff_shou"] = df_merge["buy_shou"]-df_merge["sale_shou"]
    #df_merge1 = df_merge.sort_values("buy_sale_diff_shou",ascending=False)
    df_merge1 = df_merge.sort_values("buy_sale_diff",ascending=False)
    return df_merge1

def combine_with_stock_basic_info(df_input):
    from functions.basic_info.loadBasicInfo import loadBasicInfo
    basic_info_df = loadBasicInfo().basic_in_df
    df_input['stock_index'] = [str(x).zfill(6) for x in df_input['stock_index'].tolist()] 
    df1 = pd.merge(df_input,basic_info_df,how='left',on = ["stock_index"])
    return df1
def main():
    now_date,now_date_time = get_the_datetime()  ## the now_date is like "2019_11_08"
    #now_date = "2020_05_22"
    dir_dadan = data_dict.get("DADAN")
    data_dir = os.path.join(dir_dadan,now_date)
    df1 = combine_csv_in_folder(data_dir)
    df1.columns = setColname().DADAN()
    ## merge the data
    df_merge1 = DADAN_diff_stat(df1)
    # save data
    now_date = now_date.replace("_","-")
    save_dir = dailyReport.dailyReport(now_date).save_to_daily_report()
    save_file="DADAN_200_daily_report_"+now_date+".csv"
    save_file = os.path.join(save_dir,save_file)
    df_merge1 = changeStockIndex(df_merge1,'stock_index')
    df_merge1.head(100).to_csv(save_file,encoding="utf_8_sig",index=0)
    return df_merge1
if __name__ =='__main__':
    df_merge1 = main()
    #df2 = combine_with_stock_basic_info(df_merge1)
    #print(df2.head())
    #print(df_merge1)
