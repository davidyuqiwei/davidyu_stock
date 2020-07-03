source ~/.bashrc
cd `dirname $0`
data_path="/home/davidyu/stock/data/financial_report"
combine_csv_in_folder.sh /home/davidyu/stock/data/financial_report

sed -e '/报告日期/d' $data_path"/all.csv" > $data_path/"all1.csv"
mv $data_path/"all1.csv" .
mv all1.csv all.csv
