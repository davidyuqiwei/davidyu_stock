if [ `grep -c "\-1" 150.txt` -eq '1' ];then
    echo "found"
else
    echo "not found"
fi

