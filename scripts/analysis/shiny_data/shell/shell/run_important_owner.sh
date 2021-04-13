source ~/.bashrc
cd `dirname $0`
file_out="../data/important_owner.csv"
spark-sql --hiveconf hive.cli.print.header=true -f ../sql/important_owner.sql > $file_out
sed -i 's/[\t]/,/g' $file_out
