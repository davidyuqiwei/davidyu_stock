#!/usr/bin/sh
save_dir=$stock_data"/test/"
stk_index="hk_000756"
file_name=$stk_index
f1=${save_dir}${file_name}.csv
#final_file=${file_name}_f1.csv


## run hive to export data
hive -e "set hive.cli.print.header=true;
set hive.exec.compress.output=false;
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;

select * from stock_dev.liutong_owner
where owner_name like concat('%','香港中央结算(代理人)有限公司','%')
and stock_index ='000756'
order by dt
;
" \
| sed 's/[\t]/,/g' > $f1
echo $f1
#| sed 's/[\t]/\t/g' > $f1

python ./functions/trans_csv_to_xlsx.py -f $f1




file_out="data.out"
spark-sql -f hk_increase_list.sql > $file_out
sed -i 's/[\t]/,/g' $file_out



## spark-sql conf

spark.yarn.executor.memoryOverhead=4096
soark.yarn.max.executor.failures=10
spark.yarn.max.executor.failuser=10
spark.driver.maxResultSize=2G
spark.default.parallelism=1000
spark.sql.shuffle.partitions=1000
spark.shuffle.file.buffer=64K
spark.serializer=org.apache.spark.serializer.KryoSerializer
spark.memory.useLegacyMode=true
spark.shuffle.memoryFraction=0.6
spark.storage.memoryFraction=0.2
spark.task.maxFailures=2
spark.shuffle.compress=true
spark.shuffle.spill.compress=true
spark.io.compression.codec=snappy
spark.shuffle.manager=sort
spark.shuffle.consolidateFiles=true
spark.port.maxRetries=500




