/*
    Desc: Calculate the change rate of stock over a period

    Athour:  Davidyu
    input:  Table_name, day_history
            start_date
            end date
    
    examples:
        :load /home/davidyu/stock/scripts/davidyu_stock/scripts/online/analysis/day_history/increate_rate/CalChangeRate.scala
        import org.apache.spark.sql.DataFrame


        val table="stock_dev.day_history_insert"
        val start_date="2019-06-30"
        val end_date="2019-09-25"

        val df_ch_rat = CalChangeRate.get_change(start_date,end_date,table)
        df_ch_rat.show()
    history_path:
        /home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/day_history/increase_rate
*/
import org.apache.spark.sql.DataFrame
object CalChangeRate {
    /*   within a time range the start time end time 
        start time -->  price
        end time --> price
        number of days
        change ratio --
    */
    def get_change( start_date:String,end_date:String,table:String): DataFrame ={
		val sql1 = s"""select 
		    min(struct(stock_date,adj_close,stock_index)).stock_index as stock_index,
		    min(struct(stock_date,adj_close,stock_index)).stock_date as min_date,
		    min(struct(stock_date,adj_close,stock_index)).adj_close as min_value,
		    max(struct(stock_date,adj_close,stock_index)).stock_date as max_date,
		    max(struct(stock_date,adj_close,stock_index)).adj_close as max_value,
		    round((max(struct(stock_date,adj_close,stock_index)).adj_close-min(struct(stock_date,
	                adj_close,stock_index)).adj_close)/min(struct(stock_date,adj_close,stock_index)).adj_close,3) as increaseRate,
		    count(1) as days
			from $table
			where stock_date > '$start_date' and stock_date < '$end_date' 
			group by stock_index
		    order by increaseRate
		"""
	        //val df_ch_rat = sqlContext.sql(sql1)  // stock change ratio within a time range
	        val df_ch_rat = sqlContext.sql(sql1)
	        return df_ch_rat
	        //df_ch_rat
    }
}
