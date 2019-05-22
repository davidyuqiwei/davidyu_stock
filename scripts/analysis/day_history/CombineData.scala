/*
 Desc: 1. Calculate a stock change ratio over a period 
         
        *CalChangeRate.get_change*
       
       2. Combine with the stock index and some basic information

       3. Combine with the stock owner
 
  Author : Davidyu
*/


// :load /home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/day_history/ror.scala
import org.apache.spark.sql.DataFrame
:load /home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/day_history/CalChangeRate.scala


val sqlContext = new org.apache.spark.sql.hive.HiveContext(sc)
import sqlContext.implicits._
import org.apache.spark.sql.types.StringType
object combine_data {
    /*  stock_index table 
        -- the stock list is in the table --> stock.stock_index
        -- combine the change rate with the stock list
    */
    def combine_stock_index( start_date:String,end_date:String,table:String,data_count:Int,col_in:String):DataFrame= {
	    val df_ch_rat = CalChangeRate.get_change(start_date,end_date,table) //  stock change ratio over a period
	    val sql2 = """ select * from stock.stock_index """
	    val df_stk_index =  sqlContext.sql(sql2)
	    //  ------------------------------------------------------------------
	    // combine
        // transform the column tyep and re-name "code"
	    val df_stk_index_tr = df_stk_index.withColumn("codetmp", 
	        df_stk_index("code").cast(StringType)).
            drop("code").
            withColumnRenamed("codetmp", "code")
        val diff_ratio = df_ch_rat.
            filter($"days">=data_count).
            join(df_stk_index_tr,df_ch_rat("stock_index") ===
	        df_stk_index_tr("code"))
        diff_ratio.createOrReplaceTempView("diff_ratio1")
        //val col1=Array("code","diff_ratio","name","industry","pb","holders","area")
        //val col_in=col1.mkString(",")
        val sql_in=" select  "+col_in+" from diff_ratio1 order by increaseRate desc"
        val diff_ratio_out =  sqlContext.sql(sql_in)

	    diff_ratio_out
    }
    def out_df(df1:DataFrame,start_date:String,end_date:String,table:String,ownstock_count:Int):DataFrame= {
        //  stock liutong owner table
	    //val diff_ratio = combine_stock_index(start_date,end_date,table,date_count,col_in)
        val sql_in = """select * from stock_dev.liutong_owner """
	    val df_owner = sqlContext.sql(sql_in)
	    // left_outer forbid --- column same name 
	    val df_owner_ror = df_owner.filter($"dt">=start_date).filter($"dt"<=end_date).join(df1,
	        df1("code") === df_owner("stock_index"),"left").select("owner_name",
            "stock_index","increaseRate","dt","name")
	    val df_out = df_owner_ror.groupBy("owner_name").
                agg(collect_set("name").alias("has_stocks"),
                round(avg("increaseRate"),3).alias("avg_diff"),
                count("increaseRate").alias("count")).
                orderBy(desc("avg_diff")).
                filter($"count">ownstock_count)
        df_out
    }
}
//CalChangeRate.get_change(date1,date2,table)

/*
val date1="2018-06-30"
val date2="2018-12-31"

// which table to select
val table="stock_dev.day_history_insert"
val table1="stock.stock_index"
val data_count=30
val column_in=Array("code","diff_ratio","name","industry","pb","holders","area")
val col_in=col1.mkString(",")

combine_data.combine_df(date1,date2,table,data_count,col_in)

val df_out = combine_data.out_df(date1,date2,table,data_count)
df_out.show()

val sql_in = s"""select a.*,b.name from stock_dev.liutong_owner a 
    left join  stock.stock_index b
    on a.stock_index=b.code
    where a.owner_name = '魁北克储蓄投资集团' and a.dt> '$date1' and a.dt< '$date2'"""
sqlContext.sql(sql_in)
*/


// :load /home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/day_history/CalChangeRate.scala

//val sql_in = """select * from stock_dev.liutong_owner where owner_name = '国有股' """


/*
df_out.show()



df4.filter($"stock_index" === "600118").show()
df4.filter($"owner_name" === "香港中央结算代理人有限公司").show()
val x1 = df4.filter($"owner_name" === "香港中央结算代理人有限公司").rdd.flatMap(line => { var s = line.getAs[String]("name")})

val x1 = df4.filter($"owner_name" === "香港中央结算代理人有限公司").rdd.map(y=>y.getAs[String]("name"))
df4.filter($"owner_name" === "香港中央结算代理人有限公司").pivot("name",names)

import org.apache.spark.sql.functions._
val df5 = df4.groupBy("owner_name").agg(collect_set("name"),avg("diff_ratio").alias("avg_diff"),count("diff_ratio").alias("count")).orderBy(desc("avg_diff")).filter($"count">10)

*/

/*
personDataFrame.join(orderDataFrame, personDataFrame("id_person") === 
orderDataFrame("id_person")).show()


val last_price=df1.orderBy(desc("stock_date")).limit(1).select("adj_close").collect().map(_(0))
val v1=last_price(0).toString.toDouble
val first_price=df1.orderBy("stock_date").limit(1).select("adj_close").collect().map(_(0))
val v2=first_price(0).toString.toDouble
val diff=v2-v1
val b =  diff.formatted("%.2f")
println(b)


    .collect()
val first_price=df1.orderBy("stock_date").limit(1)
    
    .collect()




*/
