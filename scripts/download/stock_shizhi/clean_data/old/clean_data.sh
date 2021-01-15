#file1="601398_shizhi.txt"
sed -i '1d' $file1
sed -i 's/var moneyFlowData=//g' $file1
#sed -i '1d' $file1
sed -i -e s/\\[/{/g  -e s/\\]//g -e s/\;//g -e s/.// -e s/.// -e s/.$// $file1
