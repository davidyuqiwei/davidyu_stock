import org.apache.spark.sql.hive.HiveContext
import org.apache.spark.sql.{DataFrame, SQLContext, SaveMode}
import org.apache.spark.sql.functions.udf
val sqlContext =new org.apache.spark.sql.hive.HiveContext(sc)

object Test {
  def main(x: Array[String]) {
    for( i <- x){
      val sql_in1=f"select * from  datamodel.store_good_kucun_$i%s_d"
      val sql_in2=f"select * from datamodel.store_good_$i%s_d"
      val sale1=sqlContext.sql(sql_in2)
      val kucun1=sqlContext.sql(sql_in1)
      val df2=kucun1.join(sale1,Seq("good_gid","store_id","date","good_id"),"left")
      df2.createOrReplaceTempView("datafr")
      val sql_out=f"create table datamodel.store_good_combine_$i%s as select * from datafr"
      sqlContext.sql(sql_out)
    }
  }
}

//val x1=Array("09")
val x1=Array("01","02","03","04","05","06","07")
Test.main(x1)
