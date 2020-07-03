from davidyu_cfg import *
from functions.pyspark_functions import *
from analysis_today_update import *
from functions.DF_process import changeStockIndex
class DaDanSql():
	@staticmethod
    def getStatusData(status):
	    sql1 = """
		select stock_index,stock_date,count(stock_index) as cnt
		from stock_test.dadan_200 
		where day > '2020-03-12' and status = '%s'
		group by stock_index,stock_date
		""" %(status)
	    return sql1


df_buy = spark.sql(DaDanSql.getStatusData("买盘")).withColumnRenamed("cnt", "buy_cnt")
df_sale = spark.sql(DaDanSql.getStatusData("卖盘")).withColumnRenamed("cnt", "sale_cnt")
df_merge = df_buy.join(df_sale,["stock_index","stock_date"],"full")
df_merge1 = df_merge.toPandas()
df_merge1 = df_merge1.fillna(0)
df_merge1['diff'] = df_merge1['buy_cnt'] - df_merge1['sale_cnt']
df_out = changeStockIndex(df_merge1,'stock_index')
df_out.to_csv('DADAN_cnt_stat.csv',index=0)


# print the random data
df1.orderBy(rand()).limit(10).show()
#df1.sample(False, 0.5, seed=0).limit(50).show()
df2 = df1.toPandas()
df_merge1 = DADAN_diff_stat(df2)





