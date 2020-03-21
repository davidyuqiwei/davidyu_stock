spark-submit \
    --executor-memory   3G \
    --driver-memory     3G \
    --conf spark.sql.autoBroadcastJoinThreshold=-1 \
    --conf spark.shuffle.file.buffer=64K \
    pyspark_v1.py
