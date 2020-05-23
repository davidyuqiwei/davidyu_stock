cd `dirname $0`
cols=$1
stock_index=$2
start_date=$3
end_date=$4
spark-submit save_data_to_csv.py \
    $cols \
    $stock_index \
    $start_date \
    $end_date

spark-submit save_data_to_csv.py 'adj_close' "('300760', '300294')" '2020-01-02' '2020-12-12'
#save_data_to_csv
# linear_reg
