#cat list.sh | sed 's/^/float  COMMENT  /g' | sed -n '='
sed "s/^/'/g" list.sh | sed "s/$/',/g" | sed 's/^/  float  COMMENT  /g' | awk '$0=""NR" "$0' | sed 's/^/    x/g' > test.txt
cp test.txt test.sql
#| sed 's/^/x/g' list.sh
