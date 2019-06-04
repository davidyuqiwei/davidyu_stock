import org.apache.log4j.{Level, Logger}
object SH_SZ_INDEX{
    def main(){
        sc.setLogLevel("ERROR")
        val log = Logger.getLogger(this.getClass)
        log.warn("this is a warn")
        log.warn("this is a warn")
		System.out.println(System.getProperty("user.dir"))
		var table_name = "stock_dev.SH_index"
		val work_dir = System.getProperty("user.dir")
		val data_file = "file://"+work_dir+"/shanghai_index_all.csv"
		val sqlContext = new org.apache.spark.sql.hive.HiveContext(sc)
		
		val csv_data = spark.read.csv(data_file)
		csv_data.show()
		csv_data.createOrReplaceTempView("history_day")
		val sql_v1 = s"""
		    truncate table $table_name
		"""
        log.error(sql_v1)
        sqlContext.sql(sql_v1)
		val sql_v2 = s"""
		    insert into table $table_name
		    select * from history_day
		"""
		log.error(sql_v2)
		//println(sql_v1)
		sqlContext.sql(sql_v2)
        log.error("+++++++++++++++++++++++++++++++++++++++")
        log.error("the program is sucess")
        log.error("+++++++++++++++++++++++++++++++++++++++")
    }
}
SH_SZ_INDEX.main()
println("+++++++++++++++++++++++++++++++++++++++")
println("the program is sucess")
println("+++++++++++++++++++++++++++++++++++++++")

//  select * from stock_dev.SH_index where stock_date >='2019-05-21'



//csv_data.toDF().insertInto("day_history")



//select max(stock_date) as date from stock_dev.day_history;
