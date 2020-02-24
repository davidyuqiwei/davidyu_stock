// this script put the   
// target csv file         to the 
// target database.table
/*
  ############################
  ####### important ##########
  ############################
  this script first 
  @clean the table
  @ put all the data into the database
*/
import org.apache.log4j.{Level, Logger}
object SH_SZ_INDEX{
    def main(FileName:String, TableName:String){
        // set the LOG level
        sc.setLogLevel("ERROR")
        val log = Logger.getLogger(this.getClass)
        log.warn("this is a warn")
        log.warn("this is a warn")
		System.out.println(System.getProperty("user.dir"))
		var table_name = TableName // set table name 
		val work_dir = System.getProperty("user.dir") // the work dir is the current dir
		val data_file = "file://"+work_dir+"/"+FileName // the full name of data file we are put into database.table
		//
        val sqlContext = new org.apache.spark.sql.hive.HiveContext(sc)
		val csv_data = spark.read.csv(data_file)
		csv_data.show()
		csv_data.createOrReplaceTempView("history_day")
		// clean the table
        /*
        val sql_v1 = s"""
		    truncate table $table_name
		"""
        log.error(sql_v1)
        sqlContext.sql(sql_v1)
        */
        sqlContext.sql("set  hive.exec.dynamic.partition.mode=nonstrict")
        sqlContext.sql("set  hive.exec.dynamic.partition=true")
        // put the new file into  database.table
		val sql_v2 = s"""
            insert into table $table_name
		    select * from history_day
		"""
		log.error(sql_v2)
		//println(sql_v1)
		sqlContext.sql(sql_v2)
        log.error("+++++++++++++++++++++++++++++++++++++++")
        log.error("ALL"+"OK")
        log.error("+++++++++++++++++++++++++++++++++++++++")
    }
}
SH_SZ_INDEX.main("all.csv","stock_dev.fin_report")
