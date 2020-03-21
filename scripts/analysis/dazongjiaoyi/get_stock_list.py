from davidyu_cfg import *
from functions.check_dataframe_to_hive import *
from functions.data_dir import *
from functions.get_datetime import *
from functions.make_dir import *


"""
SECUCODE 股票代码
SNAME   股票名称
TVAL 成交额
Zyl 折溢率
BUYERNAME 买方营业部
PRICE 成交价格
"""
def get_dazong_stock_list(dazong_date = "2020-02-20"):
    data_dir = data_dict.get("dazongjiaoyi")
    #dazong_date = "2020-02-20"
    file_name = "dazongjiaoyi_%s.csv"%(dazong_date)
    df1 = pd.read_csv(os.path.join(data_dir,file_name))
    df2 = df1.groupby(["SECUCODE","SNAME"])['TVAL'].sum().reset_index()
    #df2.sort_values("TVAL")
    df2['SECUCODE'] = [str(x).zfill(6) for x in df2['SECUCODE'].tolist() ]
    df2['trade_date'] = dazong_date
    save_dir = data_dict.get("tmp")
    save_dir = os.path.join(save_dir,"dazong_data")
    make_dir(save_dir)
    save_file = "dazongjiaoyi_stock_list_%s.csv"%(dazong_date)
    save_file = os.path.join(save_dir,save_file)
    df3 = df2[df2['TVAL']>1000]
    df2[['SECUCODE','trade_date','TVAL']].to_csv(save_file,index=0)
if __name__ == "__main__":
    start_date = sys.argv[1]
    end_date = sys.argv[2]
    date_list = getEveryDay(start_date,end_date)
    for dt in date_list:
        try:
            get_dazong_stock_list(dt)
        except:
            pass


## run download wangyi data
#os.system("sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/day_history_wangyi/run_download_day_history_wangyi.sh %s"%(save_file))
