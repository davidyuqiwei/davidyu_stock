source ~/.bashrc
cd $log_dir
first=`date +%Y-%m-%d` ## start date
second=`date -d "$first +1 day"  +"%Y-%m-%d"` # end date
echo $first
echo $second
while [ "$first" != "$second"  ]
do
    #echo $first
    first=`date -d "$first +1 day"  +"%Y-%m-%d"`
    `mkdir $log_dir/$first`
    #echo $log_dir/$first
    for i in `ls --full-time | grep -v ^d | grep $first | awk '{print $9}'`  ## list all files that modified that day
    do 
        #echo $i
        mv $i $log_dir/$first
    done
done


#for i in `ls --full-time | grep "2019-09-03" | awk '{print $9}'`
#    do 
#        echo $i
        #mv $i 2019-09-03
#    done
