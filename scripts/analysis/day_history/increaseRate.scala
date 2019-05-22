:load /home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/day_history/CombineData.scala
// :load /home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/day_history/increateRate.scala      
val date1="2018-06-30"
val date2="2018-12-31"

// which table to select
val table="stock_dev.day_history_insert"
val table1="stock.stock_index"
val data_count=30
val column_in=Array("code","increaseRate","name","industry","pb","holders","area")
val col_in=column_in.mkString(",")



val df1=combine_data.combine_stock_index(date1,date2,table,data_count,col_in)
df1.show()


val ownstock_count=10
val df_out = combine_data.out_df(df1,date1,date2,table,ownstock_count)
df_out.show()

val getout=df_out.select("has_stocks").head(10).collect()

/*
val need_check=Array("魁北克储蓄投资集团","徐开东")
val sql_in = s"""select a.*,b.name from stock_dev.liutong_owner a 
    left join  stock.stock_index b
    on a.stock_index=b.code
    where a.owner_name = '徐开东' and a.dt> '$date1' and a.dt< '$date2'"""
val check_data=sqlContext.sql(sql_in)
*/


/*
import org.apache.spark.sql.functions._
val df5 = check_data.groupBy("owner_name").agg(collect_set("name"),avg("increaseRate").alias("avg_increase"),
        count("increaseRate").alias("count")).orderBy(desc("avg_diff")).filter($"count">10)
*/
//*/
