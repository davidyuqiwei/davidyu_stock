from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
from functions.run_combine_all_csv import *
from functions.combine_with_stock_basic_info import *
from functions.jijin.jijinAnalysis import jijinAnalysis
from functions.jijin.jijinAnalysis import *

jj = jijinAnalysis().loadData()

df1 = jj.DF
#df2 = df1[df1['stock_date']=='2019-12-30']
a1 = jj.totalMoneyJijin("2020-06-30")
a2 = jj.totalMoneyJijin("2020-03-31")
a3 = pd.merge(a1,a2,how="inner",on=["stock_index"])

a3["diff"] = a3["chigu_money_y"] - a3["chigu_money_x"]
a3[a3["diff"]>0]

a1 = jj.singleStock("600598")


## 基金持有股票个数统计
jj_df1 = jj.jijinOwnCount("2020-06-30") 
stock_list1 = jijinAna.jijinOwnStat(jj_df1,1,jj.df_select)
jj_df2 = jj.jijinOwnCount("2020-03-31") 
stock_list2 = jijinAna.jijinOwnStat(jj_df2,1,jj.df_select)

#this_list = jj_df1["jijin_name"].tolist()
#last_list = jj_df2["jijin_name"].tolist()

stock_uni_list1 = stock_list1["stock_index"].unique().tolist()  
stock_uni_list2 = stock_list2["stock_index"].unique().tolist()  

ret = [ i for i in stock_uni_list1 if i not in stock_uni_list2 ]


jijin_has_count2 = jijin_has_count[jijin_has_count["stock_index"]==1]
df2[df2["jijin_name"] =="大成养老2040三年持有混合(FOF)A"]

df_list = []
for i in jijin_has_count2["jijin_name"].tolist():
    dd = df2[df2["jijin_name"]==i]
    df_list.append(dd)
t1 = pd.concat(df_list)

df2 = df1[df1['stock_date']=='2020-06-30']

df2 = df1[df1["stock_index"]=="600028"]

a1=jj.singleStock("600598")  



jj.jijinCount()

jijin_count = jijin_count(df2)




df2['chigu_money'] = df2['chigu_money'].astype(float)
df3 = df2.groupby('stock_index')['chigu_money'].sum().reset_index().sort_values('chigu_money',ascending=False)


from functions.day_history.kLines import klineDate
start_date = "2020-06-01"
stat_days = 20
pred_days = 20

stat_end_date,pred_start_date,pred_end_date = klineDate(start_date,stat_days,pred_days).make_date()

df_p1 = df2[(df2["stock_date"]>="2020-06-01")&(df2["stock_date"]<=stat_end_date)]
df_p2 = df2[(df2["stock_date"]>=pred_start_date)&(df2["stock_date"]<=pred_end_date)]

pd.merge(df_p1[["stock_index","chigu_money"]],df_p2[["stock_index","chigu_money"]],how="inner",on=["stock_index"])    



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



