source ~/.bashrc
cd $log_dir
#first=`date +%Y-%m-%d` ## start date
first="2020-02-01" ## start date
today=`date +%Y-%m-%d`
second=`date -d "$today +1 day"  +"%Y-%m-%d"` # end date
#first="2020-02-04" ## start date
#second="2020-02-09" # end date
echo "first input date: "$first
echo "second input date: "$second
while [ "$first" != "$second"  ]
do
    echo $first
    if [ ! -d "$log_dir/$first"  ]; then
        `mkdir $log_dir/$first`
        echo "make dir: "$log_dir/"$first"
    fi
    for i in `ls --full-time | grep -v ^d | grep $first | awk '{print $9}'`  ## list all files that modified that day
    do 
        mv $i $log_dir/$first
    done
    first=`date -d "$first +1 day"  +"%Y-%m-%d"`
done


#for i in `ls --full-time | grep "2019-09-03" | awk '{print $9}'`
#    do 
#        echo $i
        #mv $i 2019-09-03
#    done
