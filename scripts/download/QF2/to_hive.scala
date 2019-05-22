System.out.println(System.getProperty("user.dir"))
val work_dir=System.getProperty("user.dir")
val data_file="file://"+work_dir+"/all.csv"
//val data_file="file:///home/davidyu/stock/data/financial_report/603979_2017.csv"
val sqlContext = new org.apache.spark.sql.hive.HiveContext(sc)

val csv_data = spark.read.csv(data_file)
csv_data.show()
csv_data.createOrReplaceTempView("data_to_save")
sqlContext.sql("insert into table stock_dev.QF2 select * from data_to_save")


println("finish")
//csv_data.toDF().insertInto("day_history")



//select max(stock_date) as date from stock_dev.day_history;


