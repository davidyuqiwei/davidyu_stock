from pyspark_head import *
'''
spark = SparkSession \
    .builder \
    .appName("davidyu") \
    .enableHiveSupport() \
    .getOrCreate()

'''
def stock_basic_info():
    sql1 = """
        select * from stock.stock_index
    """
    df1 = spark.sql(sql1)
    return df1

#df1 = stock_basic_info()
#print(df1.show())
