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


def sort_data(df3,columns_in):
    df4 = df3.sort_values("TVAL",ascending=False)[columns_in]
    df4['SECUCODE'] = [str(x).zfill(6) for x in df4['SECUCODE'].tolist()]
    return df4
# 折溢率 为正的购买
def zyl_postive(df1,now_date):
    df2 = df1.copy(deep=True)
    #df2 = df1[df1['Zyl']>0]
    df2['Zyl'] = df2['Zyl'] *100
    df3 = df2.groupby(["SNAME","SECUCODE","BUYERNAME","Zyl","PRICE"])['TVAL'].sum().reset_index()
    df_sname = df2.groupby(["SNAME","SECUCODE"])['TVAL'].sum().reset_index()
    df4 = sort_data(df3,["SNAME","SECUCODE","BUYERNAME","Zyl","PRICE","TVAL"])
    df5 = sort_data(df_sname,["SNAME","SECUCODE","TVAL"])
    df4['stock_date'] = now_date
    df5['stock_date'] = now_date
    #df4 = df3.sort_values("TVAL",ascending=False)[["SNAME","SECUCODE","BUYERNAME","Zyl","PRICE","TVAL"]]
    #df4['SECUCODE'] = [str(x).zfill(6) for x in df4['SECUCODE'].tolist()]
    print(df4.head(30))
    print(df5.head(30))
    return df4,df5
if __name__ == "__main__":
	now_date,now_date_time = get_the_datetime()
	now_date = now_date.replace("_","-")
	now_date = "2020-08-03"
	data_dir = data_dict.get("dazongjiaoyi")
	file_in = "dazongjiaoyi_%s.csv"%(now_date)
	df1 = pd.read_csv(os.path.join(data_dir,file_in))
	
	report_dir = data_dict.get("daily_report")
	save_dir = os.path.join(report_dir,now_date)
	make_dir(save_dir)
	df4,df5= zyl_postive(df1,now_date)
	out_file = "dazongjiaoyi_report_%s.csv"%(now_date)
	file_name = os.path.join(save_dir,out_file) 
	df4.round(2).to_csv(file_name,index=0)


