:load /home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/day_history/CalChangeRate.scala
// :load /home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/day_history/changerate_v1.scala
import org.apache.spark.sql.DataFrame


val table="stock_dev.day_history_insert"
val start_date="2017-01-01"
val end_date="2017-12-31"

val df_ch_rat = CalChangeRate.get_change(start_date,end_date,table)
df_ch_rat.write.mode("overwrite").saveAsTable("stock_test.stock_change_date_20170101_20171231")


val start_date="2018-09-30"
val end_date="2018-12-31"

val df_ch_rat1 = CalChangeRate.get_change(start_date,end_date,table).
withColumnRenamed("increaseRate", "increaseRate1") //  stock change ratio over a period

val start_date="2018-11-30"
val end_date="2018-12-31"

val df_ch_rat2 = CalChangeRate.get_change(start_date,end_date,table) //  stock change ratio over a period

//val df_in1 = df_ch_rat.join(df_ch_rat1,df_ch_rat("stock_index")===df_ch_rat1("stock_index"),"left").

val df_in1 = df_ch_rat.join(df_ch_rat1,Seq("stock_index"),"left_outer").
select("stock_index","increaseRate", "increaseRate1")


