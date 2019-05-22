OLD_IFS="$IFS"
IFS=","
arr=(`cat t1.sh`)
IFS="$OLD_IFS"
for s in ${arr[@]}
do
   echo $s | tr -d '"'
 done
