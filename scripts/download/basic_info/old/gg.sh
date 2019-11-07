#!/usr/bin/sh
a1=`grep -r main to_hive_t1_20191107_111553_scala.log`
#echo $a1
#para1= 
a1="allok"
if cat to_hive_t1_20191107_111553_scala.log | grep "$a1">];then
    echo "ok"
else
    echo "failed"
fi

