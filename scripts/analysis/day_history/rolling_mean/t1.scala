val table = "stock_dev.day_history_insert"

val sqlContext = new org.apache.spark.sql.hive.HiveContext(sc)
import sqlContext.implicits._
import org.apache.spark.sql.types.StringType

drop table if exists stock_dev.day_history_mv_avg;
create table stock_dev.day_history_mv_avg as

val sql1 = s"""SELECT close,stock_date,stock_index, 
avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 5 PRECEDING AND 1 PRECEDING) AS mv_avg5,
avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 10 PRECEDING AND 1 PRECEDING) AS mv_avg10,
avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 15 PRECEDING AND 1 PRECEDING) AS mv_avg15,
avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 20 PRECEDING AND 1 PRECEDING) AS mv_avg20,
avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 30 PRECEDING AND 1 PRECEDING) AS mv_avg30,
avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 40 PRECEDING AND 1 PRECEDING) AS mv_avg40,
avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 50 PRECEDING AND 1 PRECEDING) AS mv_avg50,
avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 60 PRECEDING AND 1 PRECEDING) AS mv_avg60,
avg(close) OVER (PARTITION BY stock_index ORDER BY stock_date ROWS BETWEEN 120 PRECEDING AND 1 PRECEDING) AS mv_avg120
from $table
order by stock_date
"""
val df_roll_mean =  sqlContext.sql(sql1)
df_roll_mean.filter("stock_index"='000917')
df_roll_mean.filter($"stock_index"==="000917").show()
//val sql1 = s"""select close,stoc_date,class, avg(close) over(partition by stock_date range 
  //      between 1 preceding and 2 following) mm from $table """
