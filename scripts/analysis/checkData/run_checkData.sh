outfile="data.log"
sh checkData.sh > $outfile 
sed -i '/WARN/d' $outfile
sed -i '/ERROR/d' $outfile

