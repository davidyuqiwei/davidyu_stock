from davidyu_cfg import *
from functions.pyspark_functions import *
#from analysis_today_update import *
from functions.DADAN import DaDanAna
sql1 = """
select * from stock_test.dadan_100 
where day>='2020-02-14'  and day <='2020-02-25'
and stock_index='000581'
""" 

sql1 = """
select * from stock_test.dadan_200 
where day ='2020-03-12' 
""" 


sql1 = """
select * from stock_test.dadan_200 
where day >='2020-01-01' and day<='2020-04-01'
""" 

df1 = spark.sql(sql1)
# print the random data
df1.orderBy(rand()).limit(10).show()
#df1.sample(False, 0.5, seed=0).limit(50).show()
df2 = df1.toPandas()

df2['stock_date'] = df2['day']
aa = df2.groupby('stock_date').apply(lambda x: DaDanAna.DaDanAna(x).max_min().dadan_diff_stat().df_out).reset_index()
aa2 = aa[['stock_date','stock_index','buy_sale_diff']]
from functions.DF_process import changeStockIndex
aa3 = changeStockIndex(aa,'stock_index')
from functions.stock_feature.mergeData import mergeData
mergeData.loadRollingReg()

df_merge = mergeData().loadRollingReg().mergeWithRollingReg(aa3)

df2 = pd.read_csv("/home/davidyu/stock/data/tmp_data/stock_feature/rolling_regression/rolling_all.csv")

df_merge = pd.merge(df2,aa3,on=("stock_date","stock_index"))
df_merge.to_csv('test.csv',index=0)

aa2['stock_index'] = aa['stock_index'].astype(str).zfill(6)
DaDanAna.DaDanAna(df2.head(10))
df_merge1 = DADAN_diff_stat(df2)





