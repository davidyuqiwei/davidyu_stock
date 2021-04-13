source ~/.bashrc
cd `dirname $0`
file_out="../data/dfcf_bankuai.csv"
spark-sql --hiveconf hive.cli.print.header=true -f ../sql/dfcf_bankuai.sql > $file_out
sed -i 's/[\t]/,/g' $file_out
#Rscript --slave --no-save --no-restore trans_dadan_data.r
