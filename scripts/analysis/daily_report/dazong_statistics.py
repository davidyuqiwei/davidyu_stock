from davidyu_cfg import *
from functions.check_dataframe_to_hive import *
from functions.data_dir import *
from functions.get_datetime import *
from functions.make_dir import *
from functions.dazongjiaoyi.dazong_script import *
"""
SECUCODE 股票代码
SNAME   股票名称
TVAL 成交额
Zyl 折溢率
BUYERNAME 买方营业部
PRICE 成交价格
"""


def sort_data(df3,columns_in):
    df4 = df3.sort_values("TVAL",ascending=False)[columns_in]
    df4['SECUCODE'] = [str(x).zfill(6) for x in df4['SECUCODE'].tolist()]
    return df4


def get_data(now_date=None):
    if now_date == None:
        now_date,now_date_time = get_the_datetime()
        now_date = now_date.replace("_","-")
    #now_date = "2020-04-17"
    data_dir = data_dict.get("dazongjiaoyi")
    file_in = "dazongjiaoyi_%s.csv"%(now_date)
    df1 = pd.read_csv(os.path.join(data_dir,file_in))
    return df1,now_date

if __name__ == "__main__":
    #now_date = '2020-05-25'
    df1,now_date = get_data()
    dd = dazong(now_date)
    save_dir = dd.save_to_daily_report()
    print("save data to "+save_dir)
    ## all data
    df_sname,df_BUYERNAME,df_sname_BUYERNAME = dd.do_dazong_stats(0)
    out_file = "dazongjiaoyi_report_%s.csv"%(now_date)
    file_name = os.path.join(save_dir,out_file) 
    df_sname.round(2).to_csv(file_name,index=0)
    ####################################################################
    ####################################################################
    ## postive zheyilv
    df_sname,df_BUYERNAME,df_sname_BUYERNAME = dd.do_dazong_stats(1)
    pos_out_file = "dazongjiaoyi_report_pos_%s.csv"%(now_date)
    file_name = os.path.join(save_dir,pos_out_file)
    df_sname.round(2).to_csv(file_name,index=0)

