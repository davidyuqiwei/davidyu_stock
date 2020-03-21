## combine all the csv and remove the header
## in csv just keep one header
file_out1="all.csv"
data_dir1="/home/davidyu/stock/data/tmp/dazong_data"


file_out=$data_dir1"/"$file_out1
#echo $file_out
cat $data_dir1"/"*.csv > $file_out
firstline=`head -1 $file_out`
#echo $firstline
### rm column title and add in the first line
sed -i /$firstline/d  $file_out  
sed -i 1i$firstline $file_out

#rm -rf $file_out
#mv b.log $file_out

