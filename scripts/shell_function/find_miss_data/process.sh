
## unique 差集
grep -F -v -f jijin.txt stock_list.txt | sort | uniq > chaji.txt 
#comm jijin.txt stock_list.txt > chaji.txt
#sed 's/ //g' chaji.txt | sed 's/\t//g' > cha1.txt
#sort -k2n cha1.txt | uniq > cha2.txt
