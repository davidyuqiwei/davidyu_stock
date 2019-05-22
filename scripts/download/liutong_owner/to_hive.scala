System.out.println(System.getProperty("user.dir"))
val work_dir=System.getProperty("user.dir")
val data_file="file://"+work_dir+"/all.csv"

val table = "stock_dev.liutong_owner"
val sql1= s""" insert into table $table select * from data_tr"""
println(sql1)
val sqlContext = new org.apache.spark.sql.hive.HiveContext(sc)

val csv_data = spark.read.csv(data_file)
csv_data.show()
csv_data.createOrReplaceTempView("data_tr")
sqlContext.sql(sql1)

//csv_data.toDF().insertInto("day_history")

// check data
val sqlContext = new org.apache.spark.sql.hive.HiveContext(sc)
val sql_in = """select * from stock_dev.liutong_owner where owner_name = '国有股' """
sqlContext.sql(sql_in).show()

//select max(stock_date) as date from stock_dev.day_history;


