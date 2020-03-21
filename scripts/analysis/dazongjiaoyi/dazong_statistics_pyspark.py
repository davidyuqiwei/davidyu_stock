from davidyu_cfg import *
from functions.check_dataframe_to_hive import *
from functions.data_dir import *
from functions.get_datetime import *
from functions.make_dir import *
"""
secucode 股票代码
sname   股票名称
tval 成交额
zyl 折溢率
buyername 买方营业部
price 成交价格
"""


def sort_data(df3,columns_in):
    df4 = df3.sort_values("tval",ascending=False)[columns_in]
    df4['secucode'] = [str(x).zfill(6) for x in df4['secucode'].tolist()]
    return df4
# 折溢率 为正的购买
def dadan_stats(df1,groupby_col,cols_out):
    df2 = df1.copy(deep=True)
    #df2 = df1[df1['zyl']>0]
    df2['zyl'] = df2['zyl'] *100
    df3 = df2.groupby(groupby_col)['tval'].sum().reset_index()
    df_sname = df2.groupby(["sname","secucode"])['tval'].sum().reset_index()
    df4 = sort_data(df3,["sname","secucode","buyername","zyl","price","tval"])
    df5 = sort_data(df_sname,cols_out)
    #print(df4.head(30))
    #print(df5.head(30))
    return df4,df5
if __name__ == "__main__":
	now_date,now_date_time = get_the_datetime()
	now_date = now_date.replace("_","-")
	#now_date = "2020-03-05"
	data_dir = data_dict.get("dazongjiaoyi")
	file_in = "dazongjiaoyi_%s.csv"%(now_date)
	df1 = pd.read_csv(os.path.join(data_dir,file_in))
	
	report_dir = data_dict.get("daily_report")
	save_dir = os.path.join(report_dir,now_date)
	make_dir(save_dir)
	df4 = zyl_postive(df1)
	out_file = "dazongjiaoyi_report_%s.csv"%(now_date)
	file_name = os.path.join(save_dir,out_file) 
	#df4.to_csv(file_name,index=0)


