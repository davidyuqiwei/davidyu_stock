source ~/.bashrc
cd `dirname $0`
file_out="../data/fin_report.csv"
spark-sql --hiveconf hive.cli.print.header=true -f ../sql/fin_report.sql> $file_out
sed -i 's/[\t]/,/g' $file_out
