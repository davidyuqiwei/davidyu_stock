import org.apache.spark.sql.DataFrame
val sqlContext = new org.apache.spark.sql.hive.HiveContext(sc)
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
        df_ch_rat
        //df_ch_rat
    }
}
