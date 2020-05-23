from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *

"""
change_date: 报告日期
report_date: 公告日
liutong_ratio: 持股占流通比率
gudong_rank:  股东排名
num: 数量（万股）
change_type: 持股变动: 增加 减少 不变
num_change: 持股数量变动
change_ratio: 持股变化比率
"""





def get_all_date():
    cols = ["id","id2","owner_name","owner_type","stock_type","gudong_rank",
            "stock_index","stock_name","change_date","num","chigu_ratio",
            "liutong_ratio","report_date","change_type",
            "change_ratio","test1","test2","num_change"
            ]
    data_dir = data_dict.get("important_owner")
    file1 = "hk_central_2020_05_22.csv"
    df1 = pd.read_csv(os.path.join(data_dir,file1))
    #df1 = combine_csv_in_folder_raw(data_dir)
    df1.columns = cols
    df1 = df1.drop_duplicates()
    df1['stock_date'] = [x[0:10] for x in df1.change_date.tolist()]
    return df1

select_date = '2020-04-01'
df1 = get_all_date()
df2 = df1[(df1['stock_date']>= select_date)&(df1['change_type']=='增加')]

df3 = df2.sort_values(['change_ratio'])[["owner_name","stock_index","stock_name","change_ratio","change_date"]]
print(df3)
df3['stock_index'] = [str(x).zfill(6) for x in df3.stock_index.tolist()]

df3['stock_index']

#df2.groupby('stock_name').count().reset_index()



