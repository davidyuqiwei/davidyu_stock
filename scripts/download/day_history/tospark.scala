//anew File(".").getAbsolutePath()
System.out.println(System.getProperty("user.dir"))
val work_dir=System.getProperty("user.dir")
val data_file="file://"+work_dir+"/all.csv"
val csv_data = spark.read.format("com.databricks.spark.csv").option("header", "false").load(data_file)


//csv_data.write.format("parquet").save("file:////home/davidyu/data/day_history/spark/test.parquet")


import org.apache.spark.sql.SparkSession

val ss = SparkSession
.builder()
.appName(" Hive example")
.config("hive.metastore.uris", "thrift://localhost:9083")
.enableHiveSupport()
.getOrCreate()

ss.read.table("stock.stock_index")

create table stock_dev.test as
select *,row_number() over (partition by stock_index,stock_date order by stock_date) test from stock_dev.day_history;


select count(*) as count1 from stock_dev.day_history;
select count(*) as count1 from stock_dev.test;

select * from  stock_dev.test limit 10;



