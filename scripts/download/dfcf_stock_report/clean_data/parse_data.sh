file1=$1
sed -i s/data\"/Data\\n/g $file1
sed -i '1d' $file1
sed -i -e s/\\[/{/g  -e s/\\]//g -e s/\;//g -e s/.// -e s/.// -e s/.$// $file1
