System.out.println(System.getProperty("user.dir"))
val work_dir=System.getProperty("user.dir")
val data_file="file://"+work_dir+"/all.csv"

val sqlContext = new org.apache.spark.sql.hive.HiveContext(sc)

val csv_data = spark.read.csv(data_file)
csv_data.show()
csv_data.createOrReplaceTempView("history_day")
sqlContext.sql("insert into table stock_dev.day_history_insert select * from history_day")

//csv_data.toDF().insertInto("day_history")



//select max(stock_date) as date from stock_dev.day_history;


