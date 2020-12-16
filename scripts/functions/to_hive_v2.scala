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
    def data_to_hive(theFile:String,theTable:String,theType:String){
        val log = Logger.getLogger(this.getClass)
        val sqlContext = new org.apache.spark.sql.hive.HiveContext(sc)
		val csv_data = spark.read.option("header", "false").csv(theFile).dropDuplicates()
        var tableName = theTable
		csv_data.show()
		csv_data.createOrReplaceTempView("TMPTABLE")
		// clean the table
        if (theType == "whole"){
	        val sql_v1 = s"""
			    truncate table $tableName
			"""
	        sqlContext.sql(sql_v1)
        }
        sqlContext.sql("set  hive.exec.dynamic.partition.mode=nonstrict")
        sqlContext.sql("set  hive.exec.dynamic.partition=true")
        // put the new file into  database.table
		val sql_v2 = s"""
            insert into table $tableName
		    select * from TMPTABLE
		"""
        sqlContext.sql(sql_v2)
        log.error("finish table create")
    }
    //def main(FileName:String, TableName:String){
    def main(){
        // set the LOG level
        sc.setLogLevel("ERROR")
        val log = Logger.getLogger(this.getClass)
        log.warn("this is a warn")
		//val work_dir = System.getProperty("user.dir") // the work dir is the current dir
		val work_dir = "/home/davidyu/stock/scripts/davidyu_stock/scripts/cfg"
		val data_file = "file://"+work_dir+"/CONFIG" // the full name of data file we are put into database.table
        val csvData = spark.read.csv(data_file)
        var thePara = csvData.rdd.map(x=>(x.mkString.split("=")(0),x.mkString.split("=")(1))).collect().toMap
        var theFile = thePara.get("target_csv").get
        var theTable = thePara.get("dev_table").get
        try{
            var theType = thePara.get("type").get
        }catch{
            case e:Exception => println(e.getMessage)
            var theType = "whole"
        }
        var theType = thePara.get("type").get
        println("===========================================")
        var inputPara = "file: %s, table:%s, type:%s".format(theFile,theTable,theType)
        println(inputPara)
        //csvData.show() 
        data_to_hive(theFile,theTable,theType)
    }
}
SH_SZ_INDEX.main()
