cp old/000917_zhulikongpan_2020-12-27.txt test.txt
file1="test.txt"
sed -i s/jQuery1123048223496594506776_1609067355341/Data\\n/g $file1
sed -i '1d' $file1
sed -i -e s/\\[/{/g  -e s/\\]//g -e s/\;//g -e s/.// -e s/.// -e s/.$// $file1
}
