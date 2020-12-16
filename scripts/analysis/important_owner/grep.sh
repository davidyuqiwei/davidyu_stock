cd /home/davidyu/stock/data/important_owner
grep -r 2020-08-22 | grep 增加 | awk -F "," '{print $7 "," $8 "," $3}'

grep -r '{print $7 "," $8 "," $3}'

# stock index,stock name, owner name,change type, notice date 
grep -r 2020-06-30 | grep 增加 | awk -F "," '{print $7 "," $8 "," $3 "," $14 "," $13}' | uniq

grep -r 2020-06-30 | grep 增加 | awk -F "," '{print $7 "," $8 "," $3 "," $14 "," $13}' | uniq | awk -F "," '{print $1}'

grep -r 2020-06-30 | grep 增加 | awk -F "," '{print $7 "," $8 "," $3 "," $14 "," $13}' | sort | uniq -u

# stock_index,stock_name,owner_name,change_type,notice_date,change_num
grep -r 2020-06-30 | grep 增加 | awk -F "," '{print $7 "," $8 "," $3 "," $14 "," $13 "," $18}' | uniq




    	#start_date = "2020-04-30"




