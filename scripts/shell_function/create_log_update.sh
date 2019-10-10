## create log file
# run script : to_hive
# make the log : to_hive_20190610_094510_scala.log

CreateLogFile(){
    #echo "The value of the first parameter is $1 !"
    string=$1
    script_raw_name=(${string//./ })  ## script raw name xx.py --> xx
    #echo $script_raw_name"_"$DATE
    script_extention="${string#*.}"
    DATE=`date +%Y%m%d_%H%M%S`
    #echo $script_extention
    if [ $script_extention == "py" ]; then 
        Thelog=$script_raw_name"_"$DATE"_python.log"
    elif [ $script_extention == "r" ]; then 
        Thelog=$script_raw_name"_"$DATE"_Rout.log"
    elif [ $script_extention == "scala"  ]; then
        Thelog=$script_raw_name"_"$DATE"_scala.log"
    fi
    echo $Thelog
}



#funWithParam "david"
#echo $result
#echo $filename
#a1=$(funWithParam)
#echo $a1
