start_date="2017-01-01"

a1=${start_date//-/}
echo $a1

start_date="2017-01-01"
end_date="2017-12-31"
tgt_table="stock_change_rate_"${start_date//-/}"_"${end_date//-/}
echo $tgt_table

