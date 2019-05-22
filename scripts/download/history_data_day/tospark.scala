val csv_data = spark.read.format("com.databricks.spark.csv").option("header", "false").load("file:///home/davidyu/data/test.csv")

csv_data.write.format("parquet").save("file:////home/davidyu/data/day_history/spark/test.parquet")


import org.apache.spark.sql.SparkSession

val ss = SparkSession
.builder()
.appName(" Hive example")
.config("hive.metastore.uris", "thrift://localhost:9083")
.enableHiveSupport()
.getOrCreate()

ss.read.table("stock.stock_index")

