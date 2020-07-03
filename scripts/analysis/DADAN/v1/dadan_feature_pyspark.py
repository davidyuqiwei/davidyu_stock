from davidyu_cfg import *
from functions.pyspark_functions import *
#from analysis_today_update import *
from functions.DF_process import changeStockIndex
class DaDanSql():
    @staticmethod
    def getDaDanFeature():
        sql1 = """
    	select stock_index,stock_date,count(stock_index) as trade_cnt,
    	count(if(status = '买盘',stock_index, NULL)) as buy_cnt,
        count(if(status = '卖盘',status, NULL)) as sale_cnt,
        sum(if(status = '买盘',trade_num, NULL)) as buy_amount,
        sum(if(status = '卖盘',trade_num, NULL)) as sale_amount
        from stock_test.dadan_200 
    	where day > '2020-03-12' 
    	group by stock_index,stock_date
    	"""
        return sql1

aa = spark.sql(DaDanSql.getDaDanFeature())
aa.show()
'''
df_buy = spark.sql(DaDanSql.getStatusData("买盘")).withColumnRenamed("cnt", "buy_cnt")
df_sale = spark.sql(DaDanSql.getStatusData("卖盘")).withColumnRenamed("cnt", "sale_cnt")
df_merge = df_buy.join(df_sale,["stock_index","stock_date"],"full").drop("df_sale.total_trade_date")
df_merge1 = df_merge.toPandas()
df_merge1 = df_merge1.fillna(0)
df_merge1['diff'] = df_merge1['buy_cnt'] - df_merge1['sale_cnt']
df_merge1['total_trade_date'] = len(df_merge1['stock_date'].unique())
df_out = changeStockIndex(df_merge1,'stock_index')
save_dir = tmp_data_dict.get('DADAN')
df_out.to_csv(os.path.join(save_dir,'DADAN_cnt_stat.csv'),index=0)

'''






