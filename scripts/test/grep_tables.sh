file_in=$1
if [ ! -n "$file_in" ]; then
  echo "add file name : sh grep_tables.sh TABLE_NAME"
  exit 1
else
  echo $file_in
fi

echo $file_in
sed  '1i\explain' $file_in > $file_in"explain"
spark-sql -f $file_in"explain" > a.out
grep -r Scan a.out | awk -F "Scan hive" '{print $2}' | awk -F " " '{print $1}' | uniq > table_depend.sh

rm -rf $file_in"explain"


