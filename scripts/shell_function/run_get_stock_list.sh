source ~/.bashrc
# this script get all the stock index in the csv file
# e.g.
file_in=$stock_data/basic_info/stock_basic_info.csv
`awk -F "," '{print $1}' $file_in | sed '1d' > stock_list.txt`
mv stock_list.txt $stock_data"/tmp"




#sed '1d' stock_list.txt > stock_list.txt
#`tail -n 5 $file_in | awk -F "," '{print $1}' > stock_list.txt`  # tail 5 line and print the first column
#echo $stock_list > stock_list.txt

