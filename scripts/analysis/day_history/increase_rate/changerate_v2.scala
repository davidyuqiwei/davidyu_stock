:load /home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/day_history/CalChangeRate.scala
// :load /home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/day_history/changerate_v1.scala
import org.apache.spark.sql.DataFrame


val table="stock_dev.day_history_insert"
val start_date="2019-06-30"
val end_date="2019-09-25"

val df_ch_rat = CalChangeRate.get_change(start_date,end_date,table)
df_ch_rat.show()
