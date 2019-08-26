function func1(){
    count=$1
    cccc=$1
    for cont in {1..3}; do
        count=`expr $count + 1`
    done
    # 函数中使用return返回时，返回值的数据类型必须是数字
    #return $count
    echo $cccc

                  
}
