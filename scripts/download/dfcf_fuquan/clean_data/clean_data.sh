file1="601398_fuquan.txt"
#sed -i 's/klines//g' $file1
sed -i s/klines/Data\\n/g $file1
sed -i '1d' $file1
sed -i -e s/\\[/{/g  -e s/\\]//g -e s/\;//g -e s/.// -e s/.// -e s/.$// $file1


