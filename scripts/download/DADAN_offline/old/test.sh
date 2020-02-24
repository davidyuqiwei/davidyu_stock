to_database_file="the data to databse /home/davidyu/stock/data/tmp//all.csv"
if [ ! -f "$to_database_file" ];then
    echo "no data file $to_database_file";136;0c
    exit 2
else
    echo "cat all data in $to_database_file"
fi  

