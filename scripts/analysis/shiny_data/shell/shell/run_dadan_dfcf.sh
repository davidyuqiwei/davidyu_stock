source ~/.bashrc
cd `dirname $0`
file_out="../data/dadan_dfcf.csv"
spark-sql --hiveconf hive.cli.print.header=true -f ../sql/dadan_dfcf.sql > $file_out
sed -i 's/[\t]/,/g' $file_out
Rscript --slave --no-save --no-restore trans_dadan_data.r
