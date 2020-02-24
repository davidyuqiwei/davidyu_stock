from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.combine_with_stock_basic_info import *


def load_data():
    data_dir = data_dict.get("tmp")
    df1 = pd.read_csv(os.path.join(data_dir,"jijin.csv"),header=None)
    #df1.columns = [基金名称,基金代码,持仓数量,占流通股比例,持股市值,占净值比例,stock_date,stock_index]
    df1.columns = ['jijin_name','jijin_code','chicang_num','liutong_rato','chigu_price','jinzhi_ratio','stock_date','stock_index']
    return df1

def jijin_count(df2):
    a2 = df2.groupby('stock_index')['jijin_name'].count()
	a3 = a2.reset_index().sort_values('jijin_name',ascending=False)
    return a3

df1 = load_data()
#df2 = df1[df1['stock_date']=='2019-12-30']
df2 = df1[df1['stock_date']=='2019-12-31']
jijin_count = jijin_count(df2)


df2 = df1[df1['stock_date']=='2019-06-30']

df2 = df1[(df1['stock_date']=='2019-06-30')&(df1['stock_index']==428)]
df2 = df1[(df1['stock_date']=='2019-12-30')&(df1['stock_index']==917)]

df2['jijin_name']

print("total jijin number: "+str(len(df2['jijin_name'].unique())))


jijin_has_num = df2.groupby('jijin_name')['jijin_code'].count().reset_index().sort_values('jijin_code',ascending=False)

df2[df2['jijin_name'] == '富国鑫旺稳健养老目标一年持有期混合(FOF)']
df2[df2['jijin_name'] == '上投摩根安鑫回报混合C']


df2.str.contains('中庚')

df2[df2['jijin_name'].str.contains('中庚价值')]




out_name = ['name','industry','totalAssets','area']

df3 = combine_with_stock_basic_info(a3,out_name)
print(df3.head(30))

a2=df2[df2['jijin_name'].str.contains('中庚价值')]

df3 = combine_with_stock_basic_info(a3,out_name)



