#!/usr/bin/sh

#spark-sql -f index_stat.sql
#sh hive_csv.sh
#python selectFeatureByCount.py > feature_out.log
spark-submit \
    --conf spark.pyspark.driver.python=python \
    getFinReportFeature.py -start_date "2017-01-01" -end_date "2017-12-31"
# run the shell in   /home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/day_history/v1/shell
#python combineData.py
