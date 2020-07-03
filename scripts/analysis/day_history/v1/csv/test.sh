a1=$1
a2=$2
if [ ! $a1 ];then
    a1="2020"
fi
echo $a1

aa="2018-01-01"
a12=${aa//\-/}
echo $a12
