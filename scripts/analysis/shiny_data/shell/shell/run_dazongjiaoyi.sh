source ~/.bashrc
cd `dirname $0`
file_out="../data/dazongjiaoyi.csv"
spark-sql --hiveconf hive.cli.print.header=true -f ../sql/dazongjiaoyi.sql > $file_out
sed -i 's/[\t]/,/g' $file_out
