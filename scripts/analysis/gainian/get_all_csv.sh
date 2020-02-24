file_out="all.csv"

cat /home/davidyu/stock/data/gainian/gainian/*.csv > $file_out
firstline=`head -1 $file_out`
#echo $firstline
### rm column title and add in the first line
sed -i /$firstline/d  $file_out  
sed -i 1i$firstline $file_out

#rm -rf $file_out
#mv b.log $file_out

