#!/usr/bin/sh
#rm -rf day_history_bak
#cp -r day_history/ day_history_bak
#echo $1/*.csv
sed -i '1d' $1/*.csv
#cat ./day_history_bak/*.csv > ./day_history_bak/all.csv
