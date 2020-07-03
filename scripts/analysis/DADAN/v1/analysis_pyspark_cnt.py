from davidyu_cfg import *
from functions.pyspark_functions import *
#from analysis_today_update import *
from functions.DF_process import changeStockIndex
class DaDanSql():
    @staticmethod
    def getStatusData(status):
        sql1 = """
    	select stock_index,stock_date,count(distinct trade_time,stock_index) as cnt
    	from stock_test.dadan_200 
    	where day > '2019-10-19' and status = '%s'
    	group by stock_index,stock_date
    	""" %(status)
        return sql1


df_buy = spark.sql(DaDanSql.getStatusData("买盘")).withColumnRenamed("cnt", "buy_cnt")
df_sale = spark.sql(DaDanSql.getStatusData("卖盘")).withColumnRenamed("cnt", "sale_cnt")
df_merge = df_buy.join(df_sale,["stock_index","stock_date"],"full").drop("df_sale.total_trade_date")
df_merge1 = df_merge.toPandas()
df_merge1 = df_merge1.fillna(0)
df_merge1['diff'] = df_merge1['buy_cnt'] - df_merge1['sale_cnt']
df_merge1['total_trade_date'] = len(df_merge1['stock_date'].unique())
df_out = changeStockIndex(df_merge1,'stock_index')
save_dir = tmp_data_dict.get('DADAN')
df_out.drop_duplicates().to_csv(os.path.join(save_dir,'DADAN_cnt_stat.csv'),index=0)






